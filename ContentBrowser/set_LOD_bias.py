import unreal

##Intances classes of unreal engine
editor_util = unreal.EditorUtilityLibrary()
system_lib = unreal.SystemLibrary()

#get selected assets
selected_assets = editor_util.get_selected_assets()
num_assets = len(selected_assets)

#get class to chek if are texture
for asset in selected_assets:
    asset_class = asset.get_class()
    asset_name = system_lib.get_object_name(asset)
    class_name = system_lib.get_class_display_name(asset_class)

    if class_name == "Texture2D":
        ##texture = unreal.Texture2D(asset_name)
        lod_bias = asset.get_editor_property('lod_bias')
        if lod_bias == 0:
            new_lod_bias = asset.set_editor_property('lod_bias', 1)
            unreal.log("{} had a LOD Bias {} and it was change to 1".format(asset_name, lod_bias))
        else:
            unreal.log("{} has a LOD Bias {} and it was not changed".format(asset_name, lod_bias))
    else:
        unreal.log("The selected asset is not a texture, please be sure to select an asset of class Texture2D")
