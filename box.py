from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCC.Core.gp import gp_Ax2, gp_Pnt, gp_Dir
from OCC.Display.OCCViewer import rgb_color
box1 = BRepPrimAPI_MakeBox(10,10,-50).Shape()
box2 = BRepPrimAPI_MakeBox(gp_Pnt(25,0,0),10,10,50).Shape()
box3 = BRepPrimAPI_MakeBox(gp_Pnt(50,0,0),gp_Pnt(75,15,15)).Shape()
box4 = BRepPrimAPI_MakeBox(gp_Ax2(gp_Pnt(100,0,0), gp_Dir(0,1,1),
    gp_Dir(1,0,0)),10,10,50).Shape()

if __name__=="__main__":
    from OCC.Display.SimpleGui import init_display
    display, start_display, add_menu, add_function_to_menu = init_display()
    display.DisplayShape(box1,update=True,color=rgb_color(0,1,0))
    display.DisplayShape(box2,update=True,color=rgb_color(1,0,0))
    display.DisplayShape(box3,update=True,color=rgb_color(0,0,1))
    display.DisplayShape(box4,update=True,color=rgb_color(1,1,0))
    start_display()