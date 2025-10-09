@echo off
setlocal EnableExtensions EnableDelayedExpansion
set "CONFIG=%~dp0config.json"

for /f "usebackq tokens=1,* delims==" %%A in (`
  powershell -NoProfile -ExecutionPolicy Bypass -Command ^
    "$cfg = Get-Content -Raw -LiteralPath '%CONFIG%' | ConvertFrom-Json;" ^
    "Write-Output ('scriptDir=' + $cfg.scriptDir);" ^
    "Write-Output ('unrealDir=' + $cfg.unrealDir);" ^
    "Write-Output ('projectDir=' + $cfg.projectDir);"^
    "Write-Output ('unrealProjectName=' + $cfg.unrealProjectName);"
`) do set "%%A=%%B"

echo Script Directory: %scriptDir%
echo Unreal Directory: %unrealDir%
echo Project Directory: %projectDir%
echo Project Directory: %unrealProjectName%
echo.

python3 "%scriptDir%\Scripts\upscaler.py"

"%unrealDir%\Engine\Binaries\Win64\UnrealEditor-Cmd.exe" ^ "%projectDir%\%unrealProjectName%.uproject" ^ -run=pythonscript -script="%scriptDir%\Scripts\MakeUasset.py" ^ -nosplash -unattended -nullrhi -stdout -FullStdOutLogOutput ^ -DisablePlugins=Fab,OnlineSubsystemEOS,OnlineSubsystem,OnlineSubsystemSteam ^ -ini:Engine:[OnlineSubsystem]:DefaultPlatformService=None


"%unrealDir%\Engine\Binaries\Win64\UnrealEditor-Cmd.exe" ^
  "%projectDir%\%unrealProjectName%.uproject" ^
  -run=cook -targetplatform=Windows ^
  -cooksinglepackagenorefs ^
  -Map=/Game/02_Union/Asset/Character/Extnd04_Character04001/Texture/SteveFix ^
  -unversioned -stdout -FullStdOutLogOutput

python3 "%scriptDir%\Scripts\fileMover.py"

"%unrealDir%\Engine\Binaries\Win64\UnrealPak.exe" ^
 "%scriptDir%\resultingMod\y_modResult_P.pak" ^
 -Create="%scriptDir%\Dependencies\paklist_fixed.txt" -utf8output -Verbose

"%unrealDir%\Engine\Binaries\Win64\UnrealPak.exe" ^
 "%scriptDir%\resultingMod\y_modResult_P.pak" -List -utf8output

cd /d "%scriptDir%\"

retoc to-zen "%scriptDir%\resultingMod\y_modResult_P.pak" "%scriptDir%\resultingMod\y_modResult_P.utoc" --version UE5_4
