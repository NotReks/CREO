import shutil

srcUasset = r"C:\Users\Asus\Documents\Unreal Projects\SankRacists\Saved\Cooked\Windows\SankRacists\Content\02_Union\Asset\Character\Extnd04_Character04001\Texture\SonicBoomMinecraftMod.uasset"
srcUexp = r"C:\Users\Asus\Documents\Unreal Projects\SankRacists\Saved\Cooked\Windows\SankRacists\Content\02_Union\Asset\Character\Extnd04_Character04001\Texture\SonicBoomMinecraftMod.uexp"
srcUbulk = r"C:\Users\Asus\Documents\Unreal Projects\SankRacists\Saved\Cooked\Windows\SankRacists\Content\02_Union\Asset\Character\Extnd04_Character04001\Texture\SonicBoomMinecraftMod.ubulk"

destUasset = r"C:\Users\Asus\Desktop\test\fml\FinalScripts\packingDirectory\02_Union\Asset\Character\Extnd04_Character04001\Texture\SonicBoomMinecraftMod.uasset"
destUexp = r"C:\Users\Asus\Desktop\test\fml\FinalScripts\packingDirectory\02_Union\Asset\Character\Extnd04_Character04001\Texture\SonicBoomMinecraftMod.uexp"
destUbulk = r"C:\Users\Asus\Desktop\test\fml\FinalScripts\packingDirectory\02_Union\Asset\Character\Extnd04_Character04001\Texture\SonicBoomMinecraftMod.ubulk"

srcDependencyPak = r"C:\Users\Asus\Desktop\test\fml\FinalScripts\Dependencies\z_Fix_Steve_P.pak"
srcDependencyUtoc = r"C:\Users\Asus\Desktop\test\fml\FinalScripts\Dependencies\z_Fix_Steve_P.utoc"
srcDependencyUcas = r"C:\Users\Asus\Desktop\test\fml\FinalScripts\Dependencies\z_Fix_Steve_P.ucas"

destDependencyPak = r"C:\Users\Asus\Desktop\test\fml\FinalScripts\resultingMod\z_Fix_Steve_P.pak"
destDependencyUtoc = r"C:\Users\Asus\Desktop\test\fml\FinalScripts\resultingMod\z_Fix_Steve_P.utoc"
destDependencyUcas = r"C:\Users\Asus\Desktop\test\fml\FinalScripts\resultingMod\z_Fix_Steve_P.ucas"

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