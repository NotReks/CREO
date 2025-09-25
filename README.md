# CrossWorlds Skin Conversion Tool
# by REKS (@ReksArts on Twitter/X)
# MINECRAFT MODEL FIXES BY CYN (@SxlverCyn on Twitter/X)

# DISCLAIMER, YOU NEED TO HAVE UNREAL ENGINE 5.4 INSTALLED AND A SETUP PROJECT, THIS WILL LATER BE HOSTED ON A WEBSITE WHENEVER I GET ALONG TO IT TO ONLY NEED A UPLOAD OF TEXTURES
# - You need to look at every single path in these files - (paklist_fixed.txt, MakeUasset.py, makeMod.bat (ALONG WITH THEIR ALEX COUNTERPARTS), and fileMover.py to match your computer.)

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

---

## 📦 Output

- The resulting mod will be generated in the `resultingMod/` folder with the dependency fixes once you run one of the batch files.

---

## 📝 Notes

- Only **64x64 Minecraft skins** are supported for automatic conversion.  
- If you're making your own texture manually, use **CWTemplate.png** as your reference layout.  
- The conversion relies on a JSON mapping (`CWtoMCMapping.json`) to align regions from Minecraft to CrossWorlds.
