import unreal
import os

#instances of unreal classes
editor_util = unreal.EditorUtilityLibrary()
editor_asset_lib = unreal.EditorAssetLibrary()

#get the selected assetes
selected_assets = editor_util.get_selected_assets()
num_assets = len(selected_assets)
num_copies = 2
total_num_copies = num_assets * num_copies
text_label = "Duplicating Assets"
running = True

with unreal.ScopedSlowTask(total_num_copies, text_label) as slow_task:
    ##Display Slow Task
    slow_task.make_dialog()

    for asset in selected_assets:
        #get the assset name and path to be duplicated
        asset_name = asset.get_fname()
        asset_path = editor_asset_lib.get_path_name_for_loaded_asset(asset)
        source_path = os.path.dirname(asset_path)

        for i in range(num_copies):
            #if user pressed cancel button, stop
            if slow_task.should_cancel():
                running = False
                break

            new_name = "{}_{}".format(asset_name, i)
            dest_path = os.path.join(source_path, new_name)
            duplicate = editor_asset_lib.duplicate_asset(asset_path, dest_path)
            slow_task.enter_progress_frame(1)
            
            if duplicate is None:
                unreal.log_warning("Duplicate from {} at {} already exist".format(source_path, dest_path))
        
        if not running:
            break


    unreal.log("{} asset/s duplicated {} times".format(num_assets, num_copies))