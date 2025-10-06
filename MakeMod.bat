@echo off
setlocal EnableExtensions EnableDelayedExpansion
set "CONFIG=%~dp0config.json"

for /f "usebackq tokens=1,* delims==" %%A in (`
  powershell -NoProfile -ExecutionPolicy Bypass -Command ^
    "$cfg = Get-Content -Raw -LiteralPath '%CONFIG%' | ConvertFrom-Json;" ^
    "Write-Output ('scriptDir=' + $cfg.scriptDir);" ^
    "Write-Output ('unrealDir=' + $cfg.unrealDir);" ^
    "Write-Output ('projectDir=' + $cfg.projectDir);"
`) do set "%%A=%%B"

echo Script Directory:  %scriptDir%
echo Unreal Directory: %unrealDir%
echo Project Directory: %projectDir%
echo.

rem
set /p character=Enter character (Steve/Alex): 
echo.

if /I "%character%"=="Steve" (
    echo Making Alex Mod file...
    call "%~dp0steveMasterBatch.bat"
    goto :eof
) else if /I "%character%"=="Alex" (
    echo Making Alex Mod file...
    call "%~dp0alexMasterBatch.bat"
    goto :eof
) else (
    echo Invalid character. Please type Steve or Alex.
)

pause
exit /b
