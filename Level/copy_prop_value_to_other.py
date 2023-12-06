import unreal 


#Access the editor's utility library and system library
level_library = unreal.EditorActorSubsystem()

#Get the static mesh of the selected actor
selected_actor = level_library.get_selected_level_actors()

#Define Type of convertion
# 1 -> String to Map Value

case_index = 1

if case_index == 1:

    print("Copying from string to map value")

    # Define the map key to use, the source property name inside the actor, and the name of the target map
    map_key = 'ARQ'
    source_property_name =  'LevelName'
    target_prop_name = 'Specialties'

    for actor in selected_actor:
        source_property_value = actor.get_editor_property(source_property_name)

        if source_property_value is not None:
            target_map=actor.get_editor_property(target_prop_name)

            if target_map is not None and isinstance(target_map, unreal.Map):

                target_map[map_key] = source_property_value
                actor.set_editor_property(target_prop_name, target_map)

                print('Actor: {} property {} Updated.'.format(actor.get_name(), target_prop_name))


            else:
                print('Actor: {} property {} is Null or not of type MAP.'.format(actor.get_name(), target_prop_name))

        else:
            print('Actor: {} property {} is Null.'.format(actor.get_name(), source_property_name))
    
else:
    print("Define a valid case value.")