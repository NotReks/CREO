import shutil
import os
import json

config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json")

with open(config_path, "r") as f:
    config = json.load(f)

projectDir = config["projectDir"]
unrealDir = config["unrealDir"]
scriptDir = config["scriptDir"]
uProject = config["unrealProjectName"]

srcUasset = fr"{projectDir}\Saved\Cooked\Windows\{uProject}\Content\02_Union\Asset\Character\Extnd04_Character04001\Texture\SteveFix.uasset"
srcUexp = fr"{projectDir}\Saved\Cooked\Windows\{uProject}\Content\02_Union\Asset\Character\Extnd04_Character04001\Texture\SteveFix.uexp"
srcUbulk = fr"{projectDir}\Saved\Cooked\Windows\{uProject}\Content\02_Union\Asset\Character\Extnd04_Character04001\Texture\SteveFix.ubulk"

destUasset = fr"{scriptDir}\packingDirectory\02_Union\Asset\Character\Extnd04_Character04001\Texture\SteveFix.uasset"
destUexp = fr"{scriptDir}\packingDirectory\02_Union\Asset\Character\Extnd04_Character04001\Texture\SteveFix.uexp"
destUbulk = fr"{scriptDir}\packingDirectory\02_Union\Asset\Character\Extnd04_Character04001\Texture\SteveFix.ubulk"

try:
    shutil.copyfile(srcUasset, destUasset)
    shutil.copyfile(srcUexp, destUexp)
    shutil.copyfile(srcUbulk, destUbulk)
except FileNotFoundError:
    print("no file")
except Exception as e:
    print(f"{e}")