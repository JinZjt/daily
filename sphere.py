from OCC.Core.gp import gp_Pnt, gp_Ax2, gp_Dir
from OCC.Display.OCCViewer import rgb_color
import math
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeSphere

sphere1 = BRepPrimAPI_MakeSphere(100).Shape()
sphere2 = BRepPrimAPI_MakeSphere(gp_Pnt(100,0,0),100,0.5*math.pi).Shape()
sphere3 = BRepPrimAPI_MakeSphere(gp_Pnt(300,0,0),100,-0.25*math.pi,0.25*math.pi).Shape()
sphere4 = BRepPrimAPI_MakeSphere(gp_Ax2(gp_Pnt(600,0,0),gp_Dir(0,1,1),gp_Dir(1,0,0)),\
                                 100,-0.25*math.pi,0.25*math.pi,0.5*math.pi).Shape()

if __name__ == "__main__":
    from OCC.Display.SimpleGui import init_display
    display, start_display, add_menu, add_function_to_menu = init_display()
    display.DisplayShape(sphere1, update=True)
    display.DisplayShape(sphere2, update=True, color=rgb_color(1,0,1))
    display.DisplayShape(sphere3, update=True, color=rgb_color(0,1,0))
    display.DisplayShape(sphere4, update=True, color=rgb_color(1,1,0))
    start_display()