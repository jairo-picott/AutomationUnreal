import unreal 

#instance of unreal classes
editor_level_lib = unreal.EditorLevelLibrary()
editor_filter_lib = unreal.EditorFilterLibrary()

#get all actors and filter down to static mesh actors
actors = editor_level_lib.get_all_level_actors()
static_mesh = editor_filter_lib.by_class(actors, unreal.StaticMeshActor)

#Keep track of the actor index
index = 0
changed = 0

#loop trought the actors
for sma in static_mesh:

    #collect the old label and get the substring for '_'
    old_label = sma.get_actor_label()
    split_label = old_label.split('_')

    #if the label actually contains the underscore and has a substring before it
    if len(split_label) > 1:
        prefix = split_label[0]

        #Create the new label and set it to the actor
        new_label = "{}_{}".format(prefix, index)
        sma.set_actor_label(new_label)
        changed += 1

    index += 1

print("Done! Changed label for {} actors from {}.".format(changed, index))

