import unreal 

### Cerate instances of unreal classes

layer_subsystem = unreal.LayersSubsystem

#Get actor from layer NIVEIS
layer = layer_subsystem.get_layer(unreal.Name('Niveis'))
actors = layer_subsystem.get_actors_from_layer(layer)
number_actors = len(actors)

if number_actors > 0:
    unreal.log("The layer NIVEIS contain {} actors".format(number_actors))
else:
    unreal.log("No actors in NIVEIS layer")