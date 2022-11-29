import unreal 
# instaces of unreal classes

editor_asset_lib = unreal.EditorAssetLibrary()

#set source dir and options
### TODO Need to find a way to analyze just desired folder instead of all the folder in the game to avoid errors
source_dir = "/Game/DataTable"
include_subfolders = True
deleted = 0 

# get all assets in source dir
assets = editor_asset_lib.list_assets(source_dir, recursive=include_subfolders, include_folder=True)
folders = [asset for asset in assets if editor_asset_lib.does_directory_exist(asset)]

for folder in folders:
    has_assets = editor_asset_lib.does_directory_have_assets(folder)

    if not has_assets:

        #editor_asset_lib.delete_directory(folder)
        deleted += 1
        unreal.log("Folder {} without assets was deleted".format(folder))

unreal.log("Deleted {} folders without assets".format(deleted))