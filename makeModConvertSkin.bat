cd C:\Users\Asus\Desktop\test\fml\FinalScripts\

python3 convertSkin.py


"E:\UE5\UE_5.4\Engine\Binaries\Win64\UnrealEditor-Cmd.exe" ^ "C:\Users\Asus\Documents\Unreal Projects\SankRacists\SankRacists.uproject" ^ -run=pythonscript -script="C:\Users\Asus\Desktop\test\fml\FinalScripts\MakeUasset.py" ^ -nosplash -unattended -nullrhi -stdout -FullStdOutLogOutput ^ -DisablePlugins=Fab,OnlineSubsystemEOS,OnlineSubsystem,OnlineSubsystemSteam ^ -ini:Engine:[OnlineSubsystem]:DefaultPlatformService=None


"E:\UE5\UE_5.4\Engine\Binaries\Win64\UnrealEditor-Cmd.exe" ^
  "C:\Users\Asus\Documents\Unreal Projects\SankRacists\SankRacists.uproject" ^
  -run=cook -targetplatform=Windows ^
  -cooksinglepackagenorefs ^
  -Map=/Game/02_Union/Asset/Character/Extnd04_Character04001/Texture/T_Extnd04_Character04001_body_L_Bc ^
  -unversioned -stdout -FullStdOutLogOutput


cd C:\Users\Asus\Desktop\test\fml\FinalScripts\

python3 fileMover.py

"E:\UE5\UE_5.4\Engine\Binaries\Win64\UnrealPak.exe" ^
 "C:\Users\Asus\Desktop\test\fml\FinalScripts\resultingMod\modResult_P.pak" ^
 -Create="C:\Users\Asus\Desktop\test\fml\FinalScripts\paklist_fixed.txt" -utf8output -Verbose

"E:\UE5\UE_5.4\Engine\Binaries\Win64\UnrealPak.exe" ^
 "C:\Users\Asus\Desktop\test\fml\FinalScripts\resultingMod\modResult_P.pak" -List -utf8output

retoc to-zen "C:\Users\Asus\Desktop\test\fml\FinalScripts\resultingMod\modResult_P.pak" "C:\Users\Asus\Desktop\test\fml\FinalScripts\resultingMod\modResult_P.utoc" --version UE5_4