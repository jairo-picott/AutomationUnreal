import unreal


## Get libraries in variables
editor_util = unreal.EditorUtilityLibrary()
editor_asset_library = unreal.EditorAssetLibrary()
gameplay_statics = unreal.GameplayStatics()
dataprep_operations_lib = unreal.DataprepOperationsLibrary()
actor_class = unreal.Actor
static_mesh_actor_class = unreal.StaticMeshActor
system_lib = unreal.SystemLibrary()
collision_trace_flag = unreal.CollisionTraceFlag


#Select the assets
selected_assests = editor_util.get_selected_assets()
counter = 0

for asset in selected_assests:

    #Get the class and clear text name
    asset_name = system_lib.get_object_name(asset)
    asset_class = asset.get_class()
    class_name = system_lib.get_class_display_name(asset_class)

    
    if class_name == 'World':
        try:
            ##Get Actors and StaticMeshActors from the level selected 
            actors = gameplay_statics.get_all_actors_of_class(world_context_object=asset, actor_class=actor_class)
            staticMeshActors = gameplay_statics.get_all_actors_of_class(world_context_object=asset, actor_class=static_mesh_actor_class)

            
            ##Set simple collision in selected actors and StaticMeshActors
            setActorsSimpleCollision = dataprep_operations_lib.set_simple_collision(actors, unreal.ScriptCollisionShapeType.BOX)
            setStaticMeshActorsSimpleCollision = dataprep_operations_lib.set_simple_collision(staticMeshActors, unreal.ScriptCollisionShapeType.BOX)

            ##Set collision complexity in selected actors and StaticMeshActors
            setActorsCollisionComplexity = dataprep_operations_lib.set_collision_complexity(setActorsSimpleCollision, collision_trace_flag.CFT_USE_COMPLEX_AS_SIMPLE)
            setStaticMeshActorsCollisionComplexity = dataprep_operations_lib.set_collision_complexity(setStaticMeshActorsSimpleCollision, collision_trace_flag= collision_trace_flag.CFT_USE_COMPLEX_AS_SIMPLE)


            #Count the total of Actors + StaticMeshActors modified
            counter = len(actors) + len(staticMeshActors)
        except Exception as err:
            unreal.log_warning("{} of class {}, failed to set collision in actors and received this error - {}".format(asset_name, class_name, err))
            
    
    else:
        
        unreal.log_warning("The selected asset in not World class. please ensure to selected the correct asset class")

            
unreal.log("{} elements with simple collision where set and complexity collision -Use complex as simple".format(counter))


