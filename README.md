# CrossWorlds Skin Conversion Tool
# by REKS (@ReksArts on Twitter/X)

# DISCLAIMER, YOU NEED TO HAVE UNREAL ENGINE 5.4 INSTALLED AND A SETUP PROJECT, THIS WILL LATER BE HOSTED ON A WEBSITE WHENEVER I GET ALONG TO IT TO ONLY NEED A UPLOAD OF TEXTURES
# - You need to look at every single path in these files - (paklist_fixed.txt, MakeUasset.py, makeMod.bat, makeModConvertSkin.bat, convertSkin.py, and fileMover.py to match your computer.)

This tool allows you to either **manually create a texture** or **automatically convert a standard Minecraft skin (64x64)** into a CrossWorlds-compatible skin mod.

---

## 📂 Folder Setup

- **`minecraftskinHere/`**  
  Place your **64x64 Minecraft skin** PNG file here if you want to use the automatic conversion process

- **`textureHere/`**  
  Place your texture here if you've **manually created a CrossWorlds texture** and want to pack it directly without conversion.

---

## ⚙️ How to Use

# DISCLAIMER FOR AUTOMATIC CONVERSION, IT MOSTLY IS BUGGY AND UNFINISHED BECAUSE I SUCK AND COULDN'T FIGURE OUT HOW TO DO IT

### Automatic Conversion
1. Put your **64x64 Minecraft skin** inside `minecraftskinHere/`.
2. Run **`makeModConvertSkin.bat`**.  
   - This will automatically convert the Minecraft skin into the CrossWorlds format using the provided templates.  
   - The converted texture will be used to build your mod.

### Manual Texture
1. Put your **manually created CrossWorlds texture** inside `textureHere/`.
2. Run **`makeMod.bat`**.  
   - This skips the conversion step and directly uses your manual texture to build the mod.

---

## 📐 Templates

For those who want to make textures themselves:

- **`CWTemplate.png`** -> The CrossWorlds layout template  
- **`MCTemplate.png`** -> The Minecraft layout template  

These can be used to design textures by hand if you prefer not to use automatic conversion.

---

## 📦 Output

- The resulting mod will be generated in the `resultingMod/` folder once you run one of the batch files.

---

## 📝 Notes

- Only **64x64 Minecraft skins** are supported for automatic conversion.  
- If you're making your own texture manually, use **CWTemplate.png** as your reference layout.  
- The conversion relies on a JSON mapping (`CWtoMCMapping.json`) to align regions from Minecraft to CrossWorlds.
- Credit to trumank for retoc, I've packaged it here to make it easier to use. Credit - https://github.com/trumank/retoc
- Some of the code was assisted using ChatGPT 5, I've only used it for the image conversion part which automatically converts your texture to fit crossworlds because I've never done image manipulation, otherwise it's all me with a lot of googling and some help from friends for resources (Ryn for resources regarding cooking assets, and DHedge for telling me about retoc)
