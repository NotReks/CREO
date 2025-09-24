import shutil

srcUasset = r"C:\Users\Asus\Documents\Unreal Projects\SankRacists\Saved\Cooked\Windows\SankRacists\Content\02_Union\Asset\Character\Extnd04_Character04001\Texture\T_Extnd04_Character04001_body_L_Bc.uasset"
srcUexp = r"C:\Users\Asus\Documents\Unreal Projects\SankRacists\Saved\Cooked\Windows\SankRacists\Content\02_Union\Asset\Character\Extnd04_Character04001\Texture\T_Extnd04_Character04001_body_L_Bc.uexp"
srcUbulk = r"C:\Users\Asus\Documents\Unreal Projects\SankRacists\Saved\Cooked\Windows\SankRacists\Content\02_Union\Asset\Character\Extnd04_Character04001\Texture\T_Extnd04_Character04001_body_L_Bc.ubulk"

destUasset = r"C:\Users\Asus\Desktop\test\fml\FinalScripts\packingDirectory\02_Union\Asset\Character\Extnd04_Character04001\Texture\T_Extnd04_Character04001_body_L_Bc.uasset"
destUexp = r"C:\Users\Asus\Desktop\test\fml\FinalScripts\packingDirectory\02_Union\Asset\Character\Extnd04_Character04001\Texture\T_Extnd04_Character04001_body_L_Bc.uexp"
destUbulk = r"C:\Users\Asus\Desktop\test\fml\FinalScripts\packingDirectory\02_Union\Asset\Character\Extnd04_Character04001\Texture\T_Extnd04_Character04001_body_L_Bc.ubulk"

try:
    shutil.copyfile(srcUasset, destUasset)
    shutil.copyfile(srcUexp, destUexp)
    shutil.copyfile(srcUbulk, destUbulk)
except FileNotFoundError:
    print("no file")
except Exception as e:
    print(f"{e}")