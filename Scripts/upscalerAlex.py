from PIL import Image
import os, tempfile
import json

config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json")

with open(config_path, "r") as f:
    config = json.load(f)

projectDir = config["projectDir"]
unrealDir = config["unrealDir"]
scriptDir = config["scriptDir"]

path = fr"{scriptDir}\textureHere\AlexFix.png"

with Image.open(path) as img:
    w, h = img.size
    upscaled = img.resize((w * 16, h * 16), resample=Image.NEAREST)

folder, _ = os.path.split(path)
fd, tmp = tempfile.mkstemp(dir=folder, prefix=".tmp_", suffix=".png")
os.close(fd)
upscaled.save(tmp, format="PNG")
os.replace(tmp, path)
