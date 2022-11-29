import unreal


editor_asset_lib = unreal.EditorAssetLibrary
editor_level_lib = unreal.EditorLevelLibrary
editor_filter_lib = unreal.EditorFilterLibrary

material_pad = "/Game/DS/Hotel/Hotel_udatasmith/Materials/Object_ALV_TCF__30x20x11_.Object_ALV_TCF__30x20x11_"
new_material_pad = "/Game/Megascans/Surfaces/Decorative_Brick_Wall_vi0lbih/MI_Decorative_Brick_Wall_vi0lbih_2K.MI_Decorative_Brick_Wall_vi0lbih_2K"

def reaplce_material(original, replacement):
    material = editor_asset_lib.load_asset(material_pad)
    new_material = editor_asset_lib.load_asset(new_material_pad)

    if material is None:
        unreal.log_warning("The original was not found please try again")
        quit()
    elif new_material is None:
        unreal.log_warning("The new material was not found please try again")
        quit()

    try:
        editor_asset_lib.consolidate_assets(new_material, [material])
        unreal.log("The material was succesfully updated")
    except:
        unreal.log_warning("Something went wrong!")

reaplce_material(material_pad, new_material_pad)





