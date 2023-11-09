import unreal

#Import classes
actor_subsystem = unreal.EditorActorSubsystem()

#Get selected actors
selected_actors = actor_subsystem.get_selected_level_actors()

#Initialize min and max vectors with extreme values
min_vector = unreal.Vector(float('inf'), float('inf'), float('inf'))
max_vector = unreal.Vector(float('-inf'), float('-inf'), float('-inf'))

#Iterate over the actor to find the outermost points
for actor in selected_actors:
    actor_bound = actor.get_actor_bounds(False)
    min_corner = actor_bound[0] - actor_bound[1]
    max_corner = actor_bound[0] + actor_bound[1]

    #Update the min and max vectors
    min_vector.x = min(min_vector.x, min_corner.x)
    min_vector.y = min(min_vector.y, min_corner.y)
    min_vector.z = min(min_vector.z, min_corner.z)

    max_vector.x = max(max_vector.x, max_corner.x)
    max_vector.y = max(max_vector.y, max_corner.y)
    max_vector.z = max(max_vector.z, max_corner.z)

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

for vertex in vertices:
    #Update the min and max vectors
    min_vector.x = min(min_vector.x, vertex.x)
    min_vector.y = min(min_vector.y, vertex.y)
    min_vector.z = min(min_vector.z, vertex.z)

    max_vector.x = max(max_vector.x, vertex.x)
    max_vector.y = max(max_vector.y, vertex.y)
    max_vector.z = max(max_vector.z, vertex.z)

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

# Print the origin
print("Origin of the bounding box is at: {}, {}, {}".format(origin.x, origin.y, origin.z))