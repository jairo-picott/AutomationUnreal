import unreal

#Import classes
actor_subsystem = unreal.EditorActorSubsystem()
gameplay_statics = unreal.GameplayStatics()

#Get selected actors
selected_actors = actor_subsystem.get_selected_level_actors()

#Initialize min and max vectors with extreme values, and origin with 0 values
min_vector = unreal.Vector(float('inf'), float('inf'), float('inf'))
max_vector = unreal.Vector(float('-inf'), float('-inf'), float('-inf'))

total_x = 0.0
total_y = 0.0
total_z = 0.0

#Iterate over the actor to find the outermost points
for actor in selected_actors:

    #Look for the DatasmithActor class
    actor_location = actor.get_actor_location()

    total_x = total_x + actor_location.x
    total_y = total_y + actor_location.y
    total_z = total_z + actor_location.z

    #Update the min and max vectors
    min_vector.x = min(min_vector.x, actor_location.x)
    min_vector.y = min(min_vector.y, actor_location.y)
    min_vector.z = min(min_vector.z, actor_location.z)

    max_vector.x = max(max_vector.x, actor_location.x)
    max_vector.y = max(max_vector.y, actor_location.y)
    max_vector.z = max(max_vector.z, actor_location.z)

vertices = [
    unreal.Vector(min_vector.x, min_vector.y, min_vector.z),
    unreal.Vector(max_vector.x, min_vector.y, min_vector.z),
    unreal.Vector(min_vector.x, max_vector.y, min_vector.z),
    unreal.Vector(min_vector.x, min_vector.y, max_vector.z),
    unreal.Vector(max_vector.x, max_vector.y, min_vector.z),
    unreal.Vector(min_vector.z, max_vector.y, max_vector.z),
    unreal.Vector(max_vector.x, min_vector.y, max_vector.z),
    unreal.Vector(max_vector.x, max_vector.y, max_vector.z)
]


# The dimensions of the box are the differences between the max and min vectors
dimensions_x = max_vector.x - min_vector.x
dimensions_y = max_vector.y - min_vector.y
dimensions_z = max_vector.z - min_vector.z

# Print the dimensions
print("Dimensions in X: ", dimensions_x)
print("Dimensions in Y: ", dimensions_y)
print("Dimensions in Z: ", dimensions_z)

# Calculate the midpoint (origin) of the bounding box
origin_x = (min_vector.x + max_vector.x) / 2.0
origin_y = (min_vector.y + max_vector.y) / 2.0
origin_z = (min_vector.z + max_vector.z) / 2.0

origin = unreal.Vector(origin_x, origin_y, origin_z)

x = total_x / len(selected_actors)
y = total_y / len(selected_actors)
z = total_z / len(selected_actors)

# Print the origin
print("(X={},Y={},Z={})".format(x, y, z))