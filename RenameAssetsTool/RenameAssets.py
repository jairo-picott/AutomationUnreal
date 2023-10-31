import unreal
def rename_assets(search_pattern, replace_pattern):
    system_lib = unreal.SystemLibrary()
    editor_util = unreal.EditorUtilityLibrary()
    string_library = unreal.StringLibrary()

    #Get assets
    selected_assests = editor_util.get_selected_assets()
    num_assets = len(selected_assests)
    replaced = 0

    unreal.log("Selected {} asset/s".format(num_assets))

    #loop over each asset and rename
    for asset in selected_assests:
        asset_name = system_lib.get_object_name(asset)

        if string_library.contains(asset_name, search_pattern, use_case=False):
            replaced_name = string_library.replace(asset_name, search_pattern, replace_pattern)
            editor_util.rename_asset(asset, replaced_name)

            replaced += 1
            unreal.log("Replaced {} with {}".format(asset_name, replaced_name))
        else:
            unreal.log("{} did not match the search pattern, was skipped".format(asset_name))

    unreal.log("Replaced {} of {} assets".format(replaced, num_assets))

rename_assets("New","Even")