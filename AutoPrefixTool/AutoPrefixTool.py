import unreal
import json

##Intances classes of unreal engine
editor_util = unreal.EditorUtilityLibrary()
system_lib = unreal.SystemLibrary()

##prefix mapping
prefix_mapping = {}
with open("C:\\Codigo\\AutomationUnreal\\AutoPrefixTool\\prefix_mapping.json", "r") as json_file:
    prefix_mapping = json.loads(json_file.read())

##get selected assets
selected_assets = editor_util.get_selected_assets()
num_assets = len(selected_assets)
prefixed = 0

for asset in selected_assets:
    #get the class instance and clear text name
    asset_name = system_lib.get_object_name(asset)
    asset_class = asset.get_class()
    class_name = system_lib.get_class_display_name(asset_class)

    #get the prefix for the given class
    class_prefix = prefix_mapping.get(class_name, None)

    if class_prefix is None:
        unreal.log_warning("No mapping fo asset {} of type {}".format(asset_name, class_name))
        continue

    if not asset_name.startswith(class_prefix):

        #rename the asset and add the prefix
        new_name = class_prefix + asset_name
        editor_util.rename_asset(asset, new_name)
        prefixed += 1
        unreal.log("Prefixed {} of type {} with {}".format(asset_name, class_name, class_prefix))
    else:
        unreal.log("Asset {} of type {} is already prefixed with {}".format(asset_name, class_name, class_prefix))

unreal.log("Prefixed {} of {}".format(prefixed, num_assets))