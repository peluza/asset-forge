@echo off
cd /d "%~dp0"
echo --- AssetForge Installer for Windows ---
echo.
echo This script will copy 'assetforge.exe' to a system folder
echo so you can use the 'assetforge' command from anywhere.
echo.

set "EXE_NAME=assetforge.exe"

REM Case 1: Within release ZIP (exe is next to script)
if exist "%EXE_NAME%" (
    set "SOURCE=%EXE_NAME%"
) else (
    REM Case 2: Dev mode (exe is in ../dist/)
    if exist "..\dist\%EXE_NAME%" (
        set "SOURCE=..\dist\%EXE_NAME%"
    ) else (
        echo [ERROR] '%EXE_NAME%' not found.
        echo Please make sure you are in the correct folder or run 'builders\build.bat'.
        pause
        exit /b 1
    )
)

echo Source detected: %SOURCE%
echo Copying to %%LOCALAPPDATA%%\Microsoft\WindowsApps...
copy "%SOURCE%" "%LOCALAPPDATA%\Microsoft\WindowsApps\%EXE_NAME%" /Y >nul

if %errorlevel% equ 0 (
    echo.
    echo [SUCCESS] AssetForge installed correctly.
    echo.
    echo Try opening a NEW terminal and type:
    echo assetforge --help
) else (
    echo.
    echo [ERROR] Problem copying the file. Try running as Administrator.
)

echo.
pause
