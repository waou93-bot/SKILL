param(
    [Parameter(Mandatory = $true)]
    [string]$InputPath,
    [string]$OutputPath
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

if (-not (Test-Path -LiteralPath $InputPath -PathType Leaf)) {
    throw "Bookmark file not found: $InputPath"
}

$html = Get-Content -LiteralPath $InputPath -Raw
$matches = [regex]::Matches($html, '<A\b[^>]*HREF="([^"]+)"[^>]*>(.*?)</A>', [System.Text.RegularExpressions.RegexOptions]::Singleline)
$items = [System.Collections.Generic.List[object]]::new()

foreach ($match in $matches) {
    $rawUrl = [System.Net.WebUtility]::HtmlDecode($match.Groups[1].Value).Trim()
    $title = [System.Net.WebUtility]::HtmlDecode(($match.Groups[2].Value -replace '<[^>]+>', '').Trim())
    if ([string]::IsNullOrWhiteSpace($title)) { continue }

    try { $uri = [System.Uri]$rawUrl } catch { continue }
    if ($uri.Scheme -notin @('http', 'https')) { continue }

    $bookmarkHost = $uri.Host.ToLowerInvariant()
    $path = $uri.AbsolutePath.TrimEnd('/')
    $sensitive = "$bookmarkHost$path $title"
    if ($bookmarkHost -match '^(localhost|127\.0\.0\.1|0\.0\.0\.0)$') { continue }
    if ($bookmarkHost -match '(?i)(^|\.)(login|auth|sso)\.' -or
        $path -match '(?i)(^|/)(login|signin|auth|oauth|sso|session|token|csrf|password)(/|$)' -or
        $rawUrl -match '(?i)[?&](state|code|token|csrf|session|password|client_id|redirect_uri)=' ) { continue }

    $safeUrl = "$($uri.Scheme)://$bookmarkHost$path"
    $category = 'other'
    if ($sensitive -match '(?i)(github|npm|vercel|netlify|react|next|astro|svelte|three|gsap|codrops|theatre|webgl|api)') {
        $category = 'technical'
    } elseif ($sensitive -match '(?i)(dribbble|behance|awwwards|scene|design|figma|pinterest|creative|visual)') {
        $category = 'visual'
    } elseif ($sensitive -match '(?i)(pixabay|unsplash|flickr|image|video|audio|sound|music|font|youtube)') {
        $category = 'media'
    } elseif ($sensitive -match '(?i)(analytics|matomo|mixpanel|posthog|hotjar|testing|research|survey|benchmark)') {
        $category = 'research-or-ops'
    }

    $items.Add([pscustomobject]@{
        title = $title
        url = $safeUrl
        host = $bookmarkHost
        category = $category
    })
}

$result = $items | Sort-Object host, title -Unique
$json = @($result) | ConvertTo-Json -Depth 4
if ([string]::IsNullOrWhiteSpace($OutputPath)) {
    $json
} else {
    $parent = Split-Path -Parent $OutputPath
    if ($parent -and -not (Test-Path -LiteralPath $parent)) {
        New-Item -ItemType Directory -Path $parent -Force | Out-Null
    }
    Set-Content -LiteralPath $OutputPath -Value $json -Encoding UTF8
    "Indexed $(@($result).Count) sanitized bookmarks to $OutputPath"
}
