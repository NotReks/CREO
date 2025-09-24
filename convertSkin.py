from PIL import Image, ImageFilter
import json
import numpy as np
from collections import deque

mappingJson = "CWtoMCMapping.json"
mcTemplate = "MCTemplate.png"
cwTemplate = "CWTemplate.png"
inputSkin = r"C:\Users\Asus\Desktop\test\fml\FinalScripts\minecraftskinHere\minecraftSkin.png"
outputPng = r"C:\Users\Asus\Desktop\test\fml\FinalScripts\textureHere\T_Extnd04_Character04001_body_L_Bc.png"

def loadImage(src):
    if isinstance(src, Image.Image):
        img = src.convert("RGBA")
    else:
        img = Image.open(src).convert("RGBA")
        
    return img, np.array(img)

def upscaleRgba(img, scale):
    if not isinstance(img, Image.Image):
        raise TypeError(f"expected PIL.Image, got {type(img)}")
    
    if img.mode != "RGBA":
        img = img.convert("RGBA")

    if scale == 1:
        return img
    
    w, h = img.size
    r, g, b, a = img.split()

    r = r.resize((w*scale, h*scale), Image.NEAREST)
    g = g.resize((w*scale, h*scale), Image.NEAREST)
    b = b.resize((w*scale, h*scale), Image.NEAREST)
    a = a.resize((w*scale, h*scale), Image.NEAREST)

    return Image.merge("RGBA", (r, g, b, a))

def floodColorComponents(arr):
    H, W, _ = arr.shape
    backdrop = tuple(arr[0,0])
    visited = np.zeros((H,W), dtype=bool)
    comps = []

    for y in range(H):
        for x in range(W):
            if visited[y,x]:
                continue
            
            px = tuple(arr[y,x])
            if px == backdrop or px[3] == 0:
                visited[y,x] = True
                continue
            
            target = px
            q = deque([(x,y)])
            visited[y,x] = True
            pts = [(x,y)]

            while q:
                cx, cy = q.popleft()
                for nx, ny in ((cx+1,cy),(cx-1,cy),(cx,cy+1),(cx,cy-1)):
                    if 0 <= nx < W and 0 <= ny < H and not visited[ny,nx]:
                        if tuple(arr[ny,nx]) == target:
                            visited[ny,nx] = True
                            q.append((nx,ny))
                            pts.append((nx,ny))

            xs = [p[0] for p in pts]
            ys = [p[1] for p in pts]

            bbox = (min(xs), min(ys), max(xs)+1, max(ys)+1)
            comps.append({"positions": pts, "bbox": bbox, "rgba": target})

    comps.sort(key=lambda r: (r["bbox"][1], r["bbox"][0]))
    return comps, backdrop

def cwRegionsConnectivity(arr):
    H, W, _ = arr.shape
    backdrop = tuple(arr[0,0])
    mask = np.any(arr != np.array(backdrop, dtype=arr.dtype), axis=2)
    visited = np.zeros((H,W), dtype=bool)
    regs = []

    for y in range(H):
        for x in range(W):
            if visited[y,x] or not mask[y,x]:
                visited[y,x] = True
                continue
            
            q = deque([(x,y)])
            visited[y,x] = True
            pts = [(x,y)]

            while q:
                cx, cy = q.popleft()

                for nx, ny in ((cx+1,cy),(cx-1,cy),(cx,cy+1),(cx,cy-1)):
                    if 0 <= nx < W and 0 <= ny < H and not visited[ny,nx] and mask[ny,nx]:
                        visited[ny,nx] = True
                        q.append((nx,ny))
                        pts.append((nx,ny))

            xs = [p[0] for p in pts]
            ys = [p[1] for p in pts]

            bbox = (min(xs), min(ys), max(xs)+1, max(ys)+1)
            regs.append({"positions": pts, "bbox": bbox})

    regs.sort(key=lambda r: (r["bbox"][1], r["bbox"][0]))
    return regs, backdrop

def splitTopLeftRegionIntoThirds(regs):
    if not regs:
        return regs
    
    r0 = regs[0]
    x0, y0, x1, y1 = r0["bbox"]
    w = x1 - x0
    cut1 = x0 + w // 3
    cut2 = x0 + 2 * w // 3
    leftPts, midPts, rightPts = [], [], []

    for (x,y) in r0["positions"]:
        if x < cut1: leftPts.append((x,y))
        elif x < cut2: midPts.append((x,y))
        else: rightPts.append((x,y))

    def toReg(pts):
        if not pts: return None
        xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
        return {"positions": pts, "bbox": (min(xs), min(ys), max(xs)+1, max(ys)+1)}
    
    newRegs = [r for r in regs[1:]]

    for part in [leftPts, midPts, rightPts]:
        reg = toReg(part)
        if reg: newRegs.insert(0, reg)

    newRegs.sort(key=lambda r: (r["bbox"][1], r["bbox"][0]))
    return newRegs

def convertSkin(mappingJson, mcTemplate, cwTemplate, inputSkin, outputPath):
    with open(mappingJson, "r") as f:
        learnedMap = json.load(f)

    mcImg, mcArr = loadImage(mcTemplate)
    cwImg, cwArr = loadImage(cwTemplate)
    skinInit, _ = loadImage(inputSkin)
    skinImg = upscaleRgba(skinInit, 16)
    mcComps, _ = floodColorComponents(mcArr)
    cwRegs, _ = cwRegionsConnectivity(cwArr)
    cwRegs = splitTopLeftRegionIntoThirds(cwRegs)
    out = Image.new("RGBA", cwImg.size, tuple(cwArr[0,0]))
    assigns = learnedMap["assignments"]

    for a in assigns:
        cwIdx = a["cw_region_index"]
        mcIdx = a["mc_component_index"]
        cwReg = cwRegs[cwIdx]
        mcReg = mcComps[mcIdx]
        dx0, dy0, dx1, dy1 = cwReg["bbox"]
        sx0, sy0, sx1, sy1 = mcReg["bbox"]
        dw, dh = dx1 - dx0, dy1 - dy0

        srcCrop = skinImg.crop((sx0, sy0, sx1, sy1)).resize((dw, dh), resample=Image.NEAREST)
        mask = Image.new("L", (dw, dh), 0)
        mp = mask.load()

        for (x,y) in cwReg["positions"]:
            mp[x - dx0, y - dy0] = 255

        out.paste(srcCrop, (dx0, dy0), mask)

    out.save(outputPath)
    print(f"saved: {outputPath}")

if __name__ == "__main__":
    convertSkin(mappingJson, mcTemplate, cwTemplate, inputSkin, outputPng)
