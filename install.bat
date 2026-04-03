@echo off
title Install Calculator
cd /d "%~dp0"
powershell -ExecutionPolicy Bypass -File install_windows.ps1
