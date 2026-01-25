<#
Simple deploy script for copying selected files into a game's `mods` folder.
Usage (PowerShell):
  .\deploy.ps1 -Source . -Dest "C:\Path\To\Anno\mods\custom-player-colors-ewjax"
The script looks for `deploy.json` next to the script (or you can pass `-Config`) containing `include` and `exclude` glob patterns.
Patterns are relative to the `-Source` directory. Use `**` for recursive directories.
#>
param(
    [string]$Source = (Get-Location).ProviderPath,
    [string]$Dest = "",
    [string]$Config = "$PSScriptRoot\deploy.json"
)

function GlobToRegex($glob) {
    $g = $glob -replace '/','\\'
    # Escape regex special chars first
    $escaped = [Regex]::Escape($g)
    # Replace escaped ** with .* (any number of directories)
    $escaped = $escaped -replace '\\\*\\\*', '.*'
    # Replace escaped * with any characters except backslash (single path segment)
    $escaped = $escaped -replace '\\\*', '[^\\\\]*'
    # Replace escaped ? with single char
    $escaped = $escaped -replace '\\\?', '.'
    return '^' + $escaped + '$'
}

if (Test-Path $Config) {
    $cfg = Get-Content $Config -Raw | ConvertFrom-Json
    $includes = @($cfg.include) -ne $null ? $cfg.include : @()
    $excludes = @($cfg.exclude) -ne $null ? $cfg.exclude : @()
    if ($cfg.gameModsPath -and (-not $Dest)) { $Dest = $cfg.gameModsPath }
} else {
    $includes = @('modinfo.json','data\\**\\*')
    $excludes = @('working\\**')
}

if (-not $Dest) {
    Write-Error "Destination not specified. Provide -Dest or set `gameModsPath` inside deploy.json."
    exit 1
}

$srcRoot = (Get-Item $Source).FullName.TrimEnd('\')
$allFiles = Get-ChildItem -Path $srcRoot -Recurse -File -ErrorAction SilentlyContinue

$includeRegexes = @()
if ($includes) { foreach ($p in $includes) { $includeRegexes += GlobToRegex($p) } }
$excludeRegexes = @()
if ($excludes) { foreach ($p in $excludes) { $excludeRegexes += GlobToRegex($p) } }

$copied = 0
foreach ($f in $allFiles) {
    $rel = $f.FullName.Substring($srcRoot.Length).TrimStart('\')
    $isIncluded = $false
    if ($includeRegexes.Count -eq 0) { $isIncluded = $true } else {
        foreach ($r in $includeRegexes) { if ($rel -match $r) { $isIncluded = $true; break } }
    }
    if (-not $isIncluded) { continue }

    $isExcluded = $false
    foreach ($r in $excludeRegexes) { if ($rel -match $r) { $isExcluded = $true; break } }
    if ($isExcluded) { continue }

    $destPath = Join-Path -Path $Dest -ChildPath $rel
    $destDir = Split-Path $destPath -Parent
    if (-not (Test-Path $destDir)) { New-Item -ItemType Directory -Path $destDir -Force | Out-Null }
    Copy-Item -Path $f.FullName -Destination $destPath -Force
    Write-Host "Copied: $rel"
    $copied++
}

Write-Host "Deploy complete. Files copied: $copied"