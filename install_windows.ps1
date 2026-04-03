# Install Calculator to Start Menu
# Run this script once to create a Start Menu shortcut
# Right-click this file -> "Run with PowerShell"

$ErrorActionPreference = "Stop"

# Get the directory where this script is located
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$AppDir = $ScriptDir
$PywPath = Join-Path $AppDir "calculator.pyw"
$VenvPython = Join-Path $AppDir "venv\Scripts\pythonw.exe"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Calculator - Start Menu Installer" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python is installed
try {
    $pythonVersion = python --version 2>&1
    Write-Host "Found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "ERROR: Python is not installed." -ForegroundColor Red
    Write-Host "Download from: https://www.python.org/downloads/" -ForegroundColor Yellow
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit 1
}

# Create virtual environment if it doesn't exist
if (-not (Test-Path $VenvPython)) {
    Write-Host "Setting up virtual environment..." -ForegroundColor Yellow
    python -m venv (Join-Path $AppDir "venv")
    Write-Host "Installing dependencies..." -ForegroundColor Yellow
    $PipPath = Join-Path $AppDir "venv\Scripts\pip.exe"
    & $PipPath install -r (Join-Path $AppDir "requirements.txt")
    Write-Host ""
}

# Create Start Menu shortcut
$StartMenuPath = [Environment]::GetFolderPath("Programs")
$ShortcutPath = Join-Path $StartMenuPath "Calculator.lnk"

$WScriptShell = New-Object -ComObject WScript.Shell
$Shortcut = $WScriptShell.CreateShortcut($ShortcutPath)
$Shortcut.TargetPath = $VenvPython
$Shortcut.Arguments = "`"$PywPath`""
$Shortcut.WorkingDirectory = $AppDir
$Shortcut.Description = "Scientific Calculator"
$Shortcut.IconLocation = Join-Path $AppDir "assets\logo.ico"
$Shortcut.Save()

Write-Host "========================================" -ForegroundColor Green
Write-Host "  Installation Complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "You can now open Calculator from:" -ForegroundColor White
Write-Host "  - Start Menu -> Calculator" -ForegroundColor White
Write-Host "  - Double-click calculator.pyw" -ForegroundColor White
Write-Host ""
Read-Host "Press Enter to exit"
