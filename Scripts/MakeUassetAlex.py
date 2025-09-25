import os, pathlib, shutil, traceback
import unreal

SRC  = r"C:\Users\Asus\Desktop\test\fml\FinalScripts\textureHere"
DEST = "/Game/02_Union/Asset/Character/Extnd04_Character04002/Texture"
RECURSIVE = True

SCRIPT_DIR = pathlib.Path(__file__).parent.resolve()

unreal.log_warning("script running")
unreal.log_warning(f"exists? {os.path.isdir(SRC)}  DEST={DEST}")

# ensure path exists in Content Browser
if not unreal.EditorAssetLibrary.does_directory_exist(DEST):
    unreal.EditorAssetLibrary.make_directory(DEST)

pattern = "**/*.png" if RECURSIVE else "*.png"
pngs = [str(p) for p in pathlib.Path(SRC).glob(pattern)]

tasks = []
for p in pngs:
    t = unreal.AssetImportTask()
    t.filename = p
    t.destination_path = DEST
    t.automated = True
    t.save = True
    t.replace_existing = True
    tasks.append(t)

try:
    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks(tasks)
    imported = []
    for t in tasks:
        for obj in (t.imported_object_paths or []):
            unreal.log_warning(f"Imported: {obj}")

            asset = unreal.load_asset(obj)
            
            if asset and isinstance(asset, unreal.Texture2D):
                asset.never_stream = True
                assetLODGroup = unreal.TextureGroup.TEXTUREGROUP_UI
                asset.lod_group = assetLODGroup
                unreal.EditorAssetLibrary.save_loaded_asset(asset)

                imported.append(obj)

                pkg_path = unreal.EditorAssetLibrary.get_path_name_for_loaded_asset(asset)
                asset_name = os.path.basename(pkg_path).split(".")[0] + ".uasset"
                src_file = pathlib.Path(unreal.Paths.project_content_dir()) / "02_Union" / asset_name
                dst_file = SCRIPT_DIR / asset_name

                if src_file.exists():
                    shutil.copy2(src_file, dst_file)
                    unreal.log_warning(f"Copied {src_file} -> {dst_file}")
                else:
                    unreal.log_error(f"Expected uasset not found: {src_file}")

    unreal.log_warning(f"Imported total: {len(imported)}")
except Exception:
    unreal.log_error("fail import:\n" + traceback.format_exc())

unreal.SystemLibrary.quit_editor()
