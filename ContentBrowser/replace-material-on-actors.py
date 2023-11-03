import unreal

#get the libraries
editor_util = unreal.EditorUtilityLibrary()
system_lib = unreal.SystemLibrary()
editor_asset = unreal.EditorAssetLibrary()
static_mesh_subsystem = unreal.StaticMeshEditorSubsystem()

assets_path = [
    "/Game/DS/Hotel/Hotel_udatasmith/Materials/Cree_Material_Wood_Engineered_Glulam_Softwood_Horizontal",
    "/Game/DS/Hotel/Hotel_udatasmith/Geometries/Quadro_estrutural_CREE_IC_02_2-01_02_Length_9",
    "/Game/DS/Hotel/Hotel_udatasmith/Geometries/Quadro_estrutural_CREE_IC_02_2-01_02_Length_8",
    "/Game/DS/Hotel/Hotel_udatasmith/Geometries/Quadro_estrutural_CREE_IC_02_2-01_02_Length_7",
    "/Game/DS/Hotel/Hotel_udatasmith/Geometries/Quadro_estrutural_CREE_IC_02_2-01_02_Length_6",
    "/Game/DS/Hotel/Hotel_udatasmith/Geometries/Quadro_estrutural_CREE_IC_02_2-01_02_Length_5",
    "/Game/DS/Hotel/Hotel_udatasmith/Geometries/Quadro_estrutural_CREE_IC_02_2-01_02_Length_4",
    "/Game/DS/Hotel/Hotel_udatasmith/Geometries/Quadro_estrutural_CREE_IC_02_2-01_01_Length_3",
    "/Game/DS/Hotel/Hotel_udatasmith/Geometries/Quadro_estrutural_CREE_IC_02_2-02_02_Length_4",
    "/Game/DS/Hotel/Hotel_udatasmith/Geometries/Quadro_estrutural_CREE_IC_02_2-02_02_Length_3",
    "/Game/DS/Hotel/Hotel_udatasmith/Geometries/Quadro_estrutural_CREE_IC_02_2-01_01_Length_2",
    "/Game/DS/Hotel/Hotel_udatasmith/Geometries/Quadro_estrutural_CREE_IC_02_2-01_02_Length_3",
    "/Game/DS/Hotel/Hotel_udatasmith/Geometries/Quadro_estrutural_CREE_IC_02_2-01_01_Length",
    "/Game/DS/Hotel/Hotel_udatasmith/Geometries/Quadro_estrutural_CREE_IC_02_2-01_02_Length_2",
    "/Game/DS/Hotel/Hotel_udatasmith/Geometries/Quadro_estrutural_CREE_IC_02_2-01_02_Length",
    "/Game/DS/Hotel/Hotel_udatasmith/Geometries/Quadro_estrutural_CREE_IC_02_2-02_02_Length_2",
    "/Game/DS/Hotel/Hotel_udatasmith/Geometries/Quadro_estrutural_CREE_IC_02_2-02_02_Length"
]

assets = []

for asset_path in assets_path:
    asset = editor_asset.load_asset(asset_path)
    assets.append(asset)

# Get the selected assets
num_assets = len(assets)

material_pad = "/Game/DS/Hotel/Hotel_udatasmith/Materials/Cree_Material_Concrete_Precast"
new_material_pad = "/Game/Materials/Concrete_CREE_Inst.Concrete_CREE_Inst"

def reaplce_material(original, replacement):
    material = editor_asset.load_asset(material_pad)
    new_material = editor_asset.load_asset(new_material_pad)

    if material is None:
        unreal.log_warning("The original was not found please try again")
        quit()
    elif new_material is None:
        unreal.log_warning("The new material was not found please try again")
        quit()

    
    try:
        static_mesh_subsystem.editor_level.replace_mesh_components_materials_on_actors(assets, material, new_material)
        unreal.log("The material was succesfully updated on {} actor".format(num_assets))
    
    except:
        unreal.log_warning("Something went wrong!")

reaplce_material(material_pad, new_material_pad)