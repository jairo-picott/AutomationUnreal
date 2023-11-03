from os import system
import unreal
import os

#get the libraries
editor_util = unreal.EditorUtilityLibrary()
system_lib = unreal.SystemLibrary()
editor_asset = unreal.EditorAssetLibrary()
# Get the selected assets
selected_assets = editor_util.get_selected_assets()
num_assets = len(selected_assets)
celaned = 0

## hard coded parent path
parent_dir = "\\Game"

if num_assets > 0:
    asset_path = editor_asset.get_path_name_for_loaded_asset(selected_assets[0])
    parent_dir = os.path.dirname(asset_path)

for asset in selected_assets:
    
    #Get the class and clear text name
    asset_name = system_lib.get_object_name(asset)
    asset_class = asset.get_class()
    class_name = system_lib.get_class_display_name(asset_class)

    #Assemble new path and relocate
    try:
        new_path = os.path.join(parent_dir, class_name, asset_name)
        editor_asset.rename_loaded_asset(asset, new_path)
        celaned += 1
        unreal.log("Cleaned up {} to {}".format(asset_name, new_path))
    except Exception as err:
        unreal.log("Could not move {} to new location {}".format(asset_name, new_path))
        unreal.log(err)

unreal.log("Cleaned up {} of {}".format(celaned, num_assets))
