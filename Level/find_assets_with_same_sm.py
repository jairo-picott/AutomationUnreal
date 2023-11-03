import unreal 

#Access the editor's utility library and system library
level_library = unreal.EditorActorSubsystem()
system_lib = unreal.SystemLibrary()
editor_subsystem = unreal.UnrealEditorSubsystem()

# Get the currently opened level
current_level = editor_subsystem.get_editor_world()

#Specify the name of the static mesh you are looking for
static_mesh_name = "Doors_Vi-A2_Porta_Acustica_CF_VICAIMA_Portaro_EI30_AC_41dB_Guarnicao60mm__com_a"



# Get all actors in the level that have a static mesh component with the specific mesh
actors_with_sm = []
actors = unreal.GameplayStatics.get_all_actors_of_class(current_level, unreal.StaticMeshActor)

for actor in actors:
    #Assuming the actor has a StaticMeshComponent
    static_mesh_component = actor.get_component_by_class(unreal.StaticMeshComponent)
    if static_mesh_component and static_mesh_component.static_mesh:
        #Check if the static mesh's name matches what we are looking for
        if static_mesh_name == static_mesh_component.static_mesh.get_name():
            actors_with_sm.append(actor)
            #print(actor)

#Select the actors in the editor
level_library.set_selected_level_actors(actors_with_sm)

#Output how many actors were selected
print("Selected {} actors with the StaticMeshComponent {}".format(len(actors_with_sm), static_mesh_name))
