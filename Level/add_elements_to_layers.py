import unreal 

## Getting unreal classes intances
editor_util = unreal.EditorUtilityLibrary()
layer_subsystem = unreal.LayersSubsystem()
asset_tools_helper = unreal.AssetToolsHelpers()


## Getting selected assets
selected_assets = editor_util.get_selected_assets()
counter = 0

## Get all layers' names
data_layers = layer_subsystem.add_all_layer_names_to()

## Getting asset tool
asset_tool = asset_tools_helper.get_asset_tools()

## Creating an User Defined Enum
new_enum = asset_tool.create_asset("layer_name", "/Game/DataLayer", unreal.UserDefinedEnum, unreal.EnumFactory())

## Add Layer names "data_layers" to new Enum
##current_enum = unreal.load_asset("/Game/DataLayer/layer_name")
##unreal.PythonEnumLib.set_enum_items(current_enum, data_layers)


unreal.log("Enum file created with the name layer name with {} elements. ".format(len(data_layers)))

