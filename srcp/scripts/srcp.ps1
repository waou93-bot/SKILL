[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateNotNullOrEmpty()]
    [string]$Message,

    [string]$RepositoryPath = ".",

    [string]$Remote = "origin",

    [switch]$Execute,

    [switch]$CreateSystemRestorePoint
)

$ErrorActionPreference = "Stop"

function Invoke-Git {
    param(
        [Parameter(Mandatory = $true)]
        [string[]]$Arguments
    )

    $result = & git @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "Git command failed: git $($Arguments -join ' ')"
    }
    return $result
}

function Test-Administrator {
    $identity = [Security.Principal.WindowsIdentity]::GetCurrent()
    $principal = [Security.Principal.WindowsPrincipal]::new($identity)
    return $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
}

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    throw "Git is required but was not found on PATH."
}

$repoRoot = (Invoke-Git -Arguments @("-C", $RepositoryPath, "rev-parse", "--show-toplevel") | Select-Object -First 1).Trim()

$branch = & git -C $repoRoot symbolic-ref --quiet --short HEAD 2>$null
if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($branch)) {
    throw "SRCP requires a checked-out branch; detached HEAD is not supported."
}
$branch = $branch.Trim()

$remoteUrl = (Invoke-Git -Arguments @("-C", $repoRoot, "remote", "get-url", $Remote) | Select-Object -First 1).Trim()
$status = @(Invoke-Git -Arguments @("-C", $repoRoot, "status", "--short"))
$timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
$tag = "srcp/checkpoint-$timestamp"
$backupDirectory = Join-Path $repoRoot ".git\srcp-backups"
$bundlePath = Join-Path $backupDirectory "$timestamp-pre-operation.bundle"
$statusPath = Join-Path $backupDirectory "$timestamp-status.txt"

& git -C $repoRoot rev-parse --verify HEAD 2>$null | Out-Null
$hasHead = $LASTEXITCODE -eq 0

Write-Output "SRCP preview"
Write-Output "Repository: $repoRoot"
Write-Output "Branch: $branch"
Write-Output "Remote: $Remote ($remoteUrl)"
Write-Output "Checkpoint tag: $tag"
if ($hasHead) {
    Write-Output "Local bundle: $bundlePath"
} else {
    Write-Output "No existing HEAD: the checkpoint tag will be created after the first commit."
}
if ($status.Count -eq 0) {
    Write-Output "Working tree: clean"
} else {
    Write-Output "Working tree changes:"
    $status | ForEach-Object { Write-Output "  $_" }
}
if ($CreateSystemRestorePoint) {
    Write-Output "Windows system restore point: requested"
}

if (-not $Execute) {
    Write-Output "Dry run only. Re-run with -Execute after confirming the listed files and commit message."
    exit 0
}

if ($CreateSystemRestorePoint) {
    if (-not (Test-Administrator)) {
        throw "Creating a Windows system restore point requires an elevated PowerShell session. No Git changes were made."
    }
    Checkpoint-Computer -Description "SRCP $timestamp" -RestorePointType "MODIFY_SETTINGS" -ErrorAction Stop
    Write-Output "Windows system restore point created."
}

New-Item -ItemType Directory -Path $backupDirectory -Force | Out-Null
$status | Set-Content -LiteralPath $statusPath -Encoding utf8

if ($hasHead) {
    Invoke-Git -Arguments @("-C", $repoRoot, "bundle", "create", $bundlePath, "HEAD") | Out-Null
    Invoke-Git -Arguments @("-C", $repoRoot, "tag", "-a", $tag, "-m", "SRCP checkpoint before: $Message") | Out-Null
}

Invoke-Git -Arguments @("-C", $repoRoot, "add", "-A") | Out-Null
& git -C $repoRoot diff --cached --quiet
$hasStagedChanges = $LASTEXITCODE -ne 0

if ($hasStagedChanges) {
    Invoke-Git -Arguments @("-C", $repoRoot, "commit", "-m", $Message) | Out-Null
    Write-Output "Commit created."
} else {
    Write-Output "No staged changes; no empty commit created."
}

$commit = (Invoke-Git -Arguments @("-C", $repoRoot, "rev-parse", "HEAD") | Select-Object -First 1).Trim()
if (-not $hasHead) {
    Invoke-Git -Arguments @("-C", $repoRoot, "tag", "-a", $tag, "-m", "SRCP checkpoint after first commit: $Message") | Out-Null
}

Invoke-Git -Arguments @("-C", $repoRoot, "push", $Remote, "HEAD:refs/heads/$branch") | Out-Null
Invoke-Git -Arguments @("-C", $repoRoot, "push", $Remote, "refs/tags/$tag") | Out-Null

Write-Output "SRCP complete"
Write-Output "Commit: $commit"
Write-Output "Checkpoint tag: $tag"
if ($hasHead) {
    Write-Output "Local bundle: $bundlePath"
}
Write-Output "Pushed branch: $branch"
Write-Output "Pushed tag: $tag"
