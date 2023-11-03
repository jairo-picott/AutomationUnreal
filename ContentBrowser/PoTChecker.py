import unreal
import math
editor_util = unreal.EditorUtilityLibrary()


selected_assets = editor_util.get_selected_assets()
num_assets = len(selected_assets)
not_pot = 0

for asset in selected_assets:
    asset_nme = asset.get_fname()
    asset_path = asset.get_path_name()

    try:
        x_size = asset.blueprint_get_size_x()
        y_size = asset.blueprint_get_size_y()

        is_x_valid = math.log(x_size, 2).is_integer()
        is_y_valid = math.log(y_size, 2).is_integer()

        if not is_x_valid or not is_y_valid:
            unreal.log("{} is not power of two ({}, {})".format(asset_nme, x_size, y_size))
            unreal.log("It's path is  {}".format(asset_path))
            not_pot += 1
    except Exception as err:
        unreal.log("{} is not a texture - {}".format(asset_nme, err))

    

unreal.log("{} checked, {} texture found that are not power of two".format(num_assets, not_pot))