from PIL import Image
import os, tempfile

path = r"C:\Users\Asus\Desktop\test\fml\FinalScripts\textureHere\Alya.png"

with Image.open(path) as img:
    w, h = img.size
    upscaled = img.resize((w * 16, h * 16), resample=Image.NEAREST)

folder, _ = os.path.split(path)
fd, tmp = tempfile.mkstemp(dir=folder, prefix=".tmp_", suffix=".png")
os.close(fd)
upscaled.save(tmp, format="PNG")
os.replace(tmp, path)
