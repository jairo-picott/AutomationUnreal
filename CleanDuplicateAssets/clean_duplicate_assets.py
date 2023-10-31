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

#initialize a dictionary to store assets by their prefix
grouped_assets = {}

#Initialize folder index
folder_index = 0

## hard coded parent path
parent_dir = "\\Game"

## Check asset selection
if num_assets == 0:
    print('No assets selected')
    exit()

#get the asset path
asset_path = editor_asset.get_path_name_for_loaded_asset(selected_assets[0])
parent_dir = os.path.dirname(asset_path)

# Get the name without the suffix (if any)
asset_name = str(selected_assets[0].get_fname())

#Search the directoyy for similary named assets
all_assets_in_dir = editor_asset.list_assets(parent_dir)
#print(all_assets_in_dir)
matching_assets = [editor_asset.load_asset(asset) for asset in all_assets_in_dir if (asset_name in asset)]

for asset in matching_assets:
    print(asset.get_name())
