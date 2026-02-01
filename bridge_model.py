from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse
from OCC.Core.gp import gp_Vec, gp_Trsf
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_Transform
from OCC.Display.SimpleGui import init_display
# removed the material import causing the error

def create_i_girder(length, web_h, web_th, flange_w, flange_th):
    # This function builds one steel beam (I-shape)
    
    # 1. Create the vertical part (Web)
    web = BRepPrimAPI_MakeBox(length, web_th, web_h).Shape()
    
    # 2. Create the top horizontal part (Top Flange)
    top_flange = BRepPrimAPI_MakeBox(length, flange_w, flange_th).Shape()
    tf_trsf = gp_Trsf()
    # Move it to the top
    tf_trsf.SetTranslation(gp_Vec(0, -(flange_w - web_th) / 2, web_h))
    top_flange = BRepBuilderAPI_Transform(top_flange, tf_trsf, True).Shape()

    # 3. Create the bottom horizontal part (Bottom Flange)
    bot_flange = BRepPrimAPI_MakeBox(length, flange_w, flange_th).Shape()
    bf_trsf = gp_Trsf()
    # Move it to the bottom
    bf_trsf.SetTranslation(gp_Vec(0, -(flange_w - web_th) / 2, -flange_th))
    bot_flange = BRepBuilderAPI_Transform(bot_flange, bf_trsf, True).Shape()

    # 4. Glue them together
    girder = BRepAlgoAPI_Fuse(web, top_flange).Shape()
    girder = BRepAlgoAPI_Fuse(girder, bot_flange).Shape()
    
    return girder

def create_bridge_assembly(span_length, bridge_width, deck_thickness):
    # Dimensions for the steel beams (in millimeters)
    g_web_h = 1000.0   
    g_web_th = 20.0    
    g_flange_w = 300.0 
    g_flange_th = 30.0 
    
    # Create one "Master" beam
    master_girder = create_i_girder(span_length, g_web_h, g_web_th, g_flange_w, g_flange_th)
    
    # --- Place Girder 1 (Left) ---
    trsf1 = gp_Trsf()
    trsf1.SetTranslation(gp_Vec(0, 1000, 0)) 
    girder1 = BRepBuilderAPI_Transform(master_girder, trsf1, True).Shape()
    
    # --- Place Girder 2 (Right) ---
    trsf2 = gp_Trsf()
    trsf2.SetTranslation(gp_Vec(0, bridge_width - 1000 - g_web_th, 0))
    girder2 = BRepBuilderAPI_Transform(master_girder, trsf2, True).Shape()
    
    # --- Create the Concrete Deck ---
    deck = BRepPrimAPI_MakeBox(span_length, bridge_width, deck_thickness).Shape()
    
    # Move deck to sit on top of the beams
    deck_trsf = gp_Trsf()
    z_height = g_web_h + g_flange_th 
    deck_trsf.SetTranslation(gp_Vec(0, 0, z_height))
    deck = BRepBuilderAPI_Transform(deck, deck_trsf, True).Shape()
    
    return girder1, girder2, deck

if __name__ == "__main__":
    display, start_display, add_menu, add_function_to_menu = init_display()
    
    # --- CHANGE THESE NUMBERS TO RESIZE THE BRIDGE ---
    SPAN = 10000.0  # Length (10 meters)
    WIDTH = 4000.0  # Width (4 meters)
    DECK_TH = 250.0 # Thickness
    
    g1, g2, deck = create_bridge_assembly(SPAN, WIDTH, DECK_TH)
    
    # Display the bridge parts using only Colors (Removed Material arguments)
    display.DisplayShape(g1, update=True, color="BLUE")
    display.DisplayShape(g2, update=True, color="BLUE")
    display.DisplayShape(deck, update=True, color="GRAY", transparency=0.3)
    
    display.FitAll()
    start_display()