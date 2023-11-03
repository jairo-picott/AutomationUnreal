import unreal 

#instance of unreal classes
editor_level_lib = unreal.EditorLevelLibrary()
editor_filter_lib = unreal.EditorFilterLibrary()

#get all actors and filter down to specific elements
actors = editor_level_lib.get_all_level_actors()

static_mesh = editor_filter_lib.by_class(actors, unreal.StaticMeshActor)
reflection_cap = editor_filter_lib.by_class(actors, unreal.ReflectionCapture)
blueprints = editor_filter_lib.by_id_name(actors, "BP_")
player_start = editor_filter_lib.by_class(actors, unreal.PlayerStart)
text_render_actor = editor_filter_lib.by_class(actors, unreal.TextRenderActor)
world_data_layers = editor_filter_lib.by_class(actors, unreal.WorldDataLayers)
world_partition_mini_map = editor_filter_lib.by_class(actors, unreal.WorldPartitionMiniMap)

moved = 0

#create a mappin betwen folder names and arrays
mapping = {
    "StaticMeshActors": static_mesh,
    "ReflectionCaptures": reflection_cap,
    "Blueprints": blueprints,
    "PlayerStart": player_start,
    "TextRenderActor":text_render_actor,
    "WorldDataLayers": world_data_layers,
    "WorldPartitionMiniMap":world_partition_mini_map
}

for folder_name in mapping:
    # for every list of actors
    for actor in mapping[folder_name]:
        actor_name = actor.get_fname()

        actor.set_folder_path(folder_name)
        unreal.log("Moved {} into {}".format(actor_name, folder_name))

        moved += 1


unreal.log("Moved {} actors into respective folders".format(moved))