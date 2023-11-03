import unreal 
import os

#Get the classes
editor_util_lib = unreal.EditorUtilityLibrary()
editor_asset_lib = unreal.EditorAssetLibrary()

#Get selected assets
selected_assets = editor_util_lib.get_selected_assets()
num_assets = len(selected_assets)
not_used = 0

#Instantly delete assets or move to Trash folder
instant_delete = False
trash_folder = os.path.join(os.sep, "Game", "Trash")
to_be_deleted =[]

for asset in selected_assets:
    # get the full path of the asset
    asset_name = asset.get_fname()
    asset_path = editor_asset_lib.get_path_name_for_loaded_asset(asset)

    #get list of references for this asset
    asset_references = editor_asset_lib.find_package_referencers_for_asset(asset_path)

    if(len(asset_references)) == 0:
        to_be_deleted.append(asset)

for asset in to_be_deleted:
    asset_name = asset.get_fname()

    #Instant delete
    if instant_delete:
            
        deleted = editor_asset_lib.delete_loaded_asset(asset)

        if not deleted:
            unreal.log_warning("Asset {} could not be deleted".format(asset_name))
            continue

        not_used += 1
    
    #Move to trash folder
    else:
        new_path = os.path.join(trash_folder, str(asset_name))
        moved = editor_asset_lib.rename_loaded_asset(asset, new_path)

        if not moved:
            unreal.log_warning("Asset {} could not me moved to Trash".format(asset_name))
            continue

        not_used += 1

if instant_delete:
    unreal.log("{} of {} to be deleted assets, of {} selected, removed".format(not_used, len(to_be_deleted), num_assets))
else:
    unreal.log("{} of {} to be deleted assets, of {} selected, moved to Trash".format(not_used, len(to_be_deleted), num_assets))


   