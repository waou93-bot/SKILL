[CmdletBinding()]
param(
    [string]$DestinationRoot = (Join-Path $env:USERPROFILE '.agents\skills'),
    [switch]$Update
)
$ErrorActionPreference = 'Stop'
$packagePath = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..'))
$rootPath = [IO.Path]::GetFullPath($DestinationRoot)
$targetPath = [IO.Path]::GetFullPath((Join-Path $rootPath 'newsit-seo'))
if (-not $targetPath.StartsWith($rootPath.TrimEnd('\') + '\', [StringComparison]::OrdinalIgnoreCase)) {
    throw 'Installation target must remain inside the chosen skill root.'
}
if ($targetPath -eq $packagePath) { throw 'Source and destination are identical.' }
if ($targetPath.StartsWith($packagePath.TrimEnd('\') + '\', [StringComparison]::OrdinalIgnoreCase) -or
    $packagePath.StartsWith($targetPath.TrimEnd('\') + '\', [StringComparison]::OrdinalIgnoreCase)) {
    throw 'Source and destination cannot be nested.'
}
if (Test-Path -LiteralPath $targetPath) {
    if (-not $Update) { throw 'An installation already exists. Review it before using -Update.' }
    $backupRoot = Join-Path ([IO.Directory]::GetParent($rootPath).FullName) 'skill-install-backups'
    $backupPath = Join-Path $backupRoot ('newsit-seo-' + (Get-Date -Format 'yyyyMMdd-HHmmss-fff'))
    New-Item -ItemType Directory -Path $backupRoot -Force | Out-Null
    Copy-Item -LiteralPath $targetPath -Destination $backupPath -Recurse
}
New-Item -ItemType Directory -Path $targetPath -Force | Out-Null
Get-ChildItem -LiteralPath $packagePath -Force | ForEach-Object {
    Copy-Item -LiteralPath $_.FullName -Destination $targetPath -Recurse -Force
}
Get-ChildItem -LiteralPath $packagePath -File -Recurse | ForEach-Object {
    $relativePath = $_.FullName.Substring($packagePath.TrimEnd('\').Length + 1)
    $installedPath = Join-Path $targetPath $relativePath
    if (-not (Test-Path -LiteralPath $installedPath) -or
        (Get-FileHash -LiteralPath $_.FullName).Hash -ne (Get-FileHash -LiteralPath $installedPath).Hash) {
        throw ('Installed file differs from source: ' + $relativePath)
    }
}
Write-Output ('Installed Newsit SEO at ' + $targetPath + '. Refresh the host skill catalog if needed.')
