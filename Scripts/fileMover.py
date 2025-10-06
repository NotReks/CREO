import shutil
import os
import json

config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json")

with open(config_path, "r") as f:
    config = json.load(f)

projectDir = config["projectDir"]
unrealDir = config["unrealDir"]
scriptDir = config["scriptDir"]

srcUasset = fr"{projectDir}\Saved\Cooked\Windows\SankRacists\Content\02_Union\Asset\Character\Extnd04_Character04001\Texture\SonicBoomMinecraftMod.uasset"
srcUexp = fr"{projectDir}\Saved\Cooked\Windows\SankRacists\Content\02_Union\Asset\Character\Extnd04_Character04001\Texture\SonicBoomMinecraftMod.uexp"
srcUbulk = fr"{projectDir}\Saved\Cooked\Windows\SankRacists\Content\02_Union\Asset\Character\Extnd04_Character04001\Texture\SonicBoomMinecraftMod.ubulk"

destUasset = fr"{scriptDir}\packingDirectory\02_Union\Asset\Character\Extnd04_Character04001\Texture\SonicBoomMinecraftMod.uasset"
destUexp = fr"{scriptDir}\packingDirectory\02_Union\Asset\Character\Extnd04_Character04001\Texture\SonicBoomMinecraftMod.uexp"
destUbulk = fr"{scriptDir}\packingDirectory\02_Union\Asset\Character\Extnd04_Character04001\Texture\SonicBoomMinecraftMod.ubulk"

srcDependencyPak = fr"{scriptDir}\Dependencies\z_Fix_Steve_P.pak"
srcDependencyUtoc = fr"{scriptDir}\Dependencies\z_Fix_Steve_P.utoc"
srcDependencyUcas = fr"{scriptDir}\Dependencies\z_Fix_Steve_P.ucas"

destDependencyPak = fr"{scriptDir}\resultingMod\z_Fix_Steve_P.pak"
destDependencyUtoc = fr"{scriptDir}\resultingMod\z_Fix_Steve_P.utoc"
destDependencyUcas = fr"{scriptDir}\resultingMod\z_Fix_Steve_P.ucas"

try:
    shutil.copyfile(srcUasset, destUasset)
    shutil.copyfile(srcUexp, destUexp)
    shutil.copyfile(srcUbulk, destUbulk)
    
    shutil.copyfile(srcDependencyPak, destDependencyPak)
    shutil.copyfile(srcDependencyUtoc, destDependencyUtoc)
    shutil.copyfile(srcDependencyUcas, destDependencyUcas)
except FileNotFoundError:
    print("no file")
except Exception as e:
    print(f"{e}")