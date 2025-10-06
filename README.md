# CrossWorlds Skin Conversion Tool
# SCRIPT BY REKS (@ReksArts on Twitter/X)
# MINECRAFT MODEL FIXES BY CYN (@SxlverCyn on Twitter/X)

# DISCLAIMER, YOU NEED TO HAVE UNREAL ENGINE 5.4 INSTALLED AND A SETUP PROJECT, THIS WILL LATER BE HOSTED ON A WEBSITE WHENEVER I GET ALONG TO IT TO ONLY NEED A UPLOAD OF TEXTURES
# - CHANGE THE FILE PATHS IN CONFIG.JSON
# - ALSO ADJUST THE PAKLIST DIRECTORIES IN THE DEPENDENCIES FOLDER
# - MAKE SURE PYTHON 3.12 IS INSTALLED (MICROSOFT STORE) !!

---

## 📂 Folder Setup

- **`textureHere/`**  
  Place your texture here.

---

## ⚙️ How to Use

1. Put your texture inside `textureHere/`.
2. Run **`makeModSteve.bat`** or **`makeModAlex.bat`**.  
   - Make sure you name the png file for Steve "SonicBoomMinecraftMod"
   - Make sure you name the png file for Alex "Alya"
   - Make sure you drag the z_FixAlex_P.pak,utoc,ucas from the Dependencies folder to your ~Mods folder too because fuck me python wants to be stupid

---

## 📦 Output

- The resulting mod will be generated in the `resultingMod/` folder with the dependency fixes once you run one of the batch files.

---

## 📝 Notes

- Only **64x64 Minecraft skins** are supported for automatic conversion.  
- If the skin is blurry after creation then manually upscale it 16x.
- If you have trouble with the texture, edit the resolution to be 1024x1023.