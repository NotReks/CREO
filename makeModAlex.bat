"E:\UE5\UE_5.4\Engine\Binaries\Win64\UnrealEditor-Cmd.exe" ^ "C:\Users\Asus\Documents\Unreal Projects\SankRacists\SankRacists.uproject" ^ -run=pythonscript -script="C:\Users\Asus\Desktop\test\fml\FinalScripts\Scripts\MakeUassetAlex.py" ^ -nosplash -unattended -nullrhi -stdout -FullStdOutLogOutput ^ -DisablePlugins=Fab,OnlineSubsystemEOS,OnlineSubsystem,OnlineSubsystemSteam ^ -ini:Engine:[OnlineSubsystem]:DefaultPlatformService=None


"E:\UE5\UE_5.4\Engine\Binaries\Win64\UnrealEditor-Cmd.exe" ^
  "C:\Users\Asus\Documents\Unreal Projects\SankRacists\SankRacists.uproject" ^
  -run=cook -targetplatform=Windows ^
  -cooksinglepackagenorefs ^
  -Map=/Game/02_Union/Asset/Character/Extnd04_Character04002/Texture/Alya ^
  -unversioned -stdout -FullStdOutLogOutput


cd C:\Users\Asus\Desktop\test\fml\FinalScripts\Scripts\

python3 fileMoverAlex.py

"E:\UE5\UE_5.4\Engine\Binaries\Win64\UnrealPak.exe" ^
 "C:\Users\Asus\Desktop\test\fml\FinalScripts\resultingMod\y_modResultAlex_P.pak" ^
 -Create="C:\Users\Asus\Desktop\test\fml\FinalScripts\Dependencies\paklist_fixedAlex.txt" -utf8output -Verbose

"E:\UE5\UE_5.4\Engine\Binaries\Win64\UnrealPak.exe" ^
 "C:\Users\Asus\Desktop\test\fml\FinalScripts\resultingMod\y_modResultAlex_P.pak" -List -utf8output

cd C:\Users\Asus\Desktop\test\fml\FinalScripts\

retoc to-zen "C:\Users\Asus\Desktop\test\fml\FinalScripts\resultingMod\y_modResultAlex_P.pak" "C:\Users\Asus\Desktop\test\fml\FinalScripts\resultingMod\y_modResultAlex_P.utoc" --version UE5_4

