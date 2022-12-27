from vpython import *
import vpython
from time import sleep
from tkinter import Tk

from os import getcwd as mypath

# I don't want to input my FPS every time I test my program so I do this for later use (:
test_path = mypath().lower().startswith("C:\\Users\\inicio".lower())
fps = 60

class SuperAwesomeAndComplexTree():
    def super_tree(self, tab : int = 10):
        to_print = ""
        # Leaves and branches and those pointy thingies, basically the top of the tree
        for x in range(tab): to_print += " "*(tab-x) + "*"*(x) + "*"*(x-1) + "\n"
        # Log, trunk, idk what was the word in english lol
        for x in range(int(tab/4)): to_print += " "*(tab-1) + "*\n"
        # Print the whole super cool and complex tree...
        for x in to_print:
            print(x, end="")
            sleep(((1/1)/fps) if not test_path else 0)

class MehTree():

    def get_curr_screen_geometry(self):
        """
        Workaround to get the size of the current screen in a multi-screen setup.

        Returns:
            geometry (str): The standard Tk geometry string.
                [width]x[height]+[left]+[top]
        """
        root = Tk()
        root.update_idletasks()
        root.attributes('-fullscreen', True)
        root.state('iconic')
        geometry = root.winfo_geometry()
        root.destroy()
        return geometry
        
    def __init__(self) -> None:
        # I don't remember what I wanted to do here and I don't use it yet lol
        w = int(self.get_curr_screen_geometry().split("x")[0]) * .60
        h = int(self.get_curr_screen_geometry().split("x")[1].split("+")[0]) *.60
        print(f"Working with size: {w}*60%, {h}*60%")
        scene = canvas(width=w, height=h,background=color.black, 
        center=vector(0,0,0), ambient=color.black, title='''
        <head><title>Home</title></head>
        </script>
        document.body.style.backgroundColor = "#BB2528";
        <script>
        
        <style>
        </style>
        <h1><strong style="color=#146B3A;background-color:#BB2528;">Holis</strong></h1>
        ''',
        caption='''
        <strong>Hey!</strong>
        ''')
        
        pass

    def learning_vpython(self):
        mRadius = .75
        wallThickness=.1
        ten = 10
        roomWidth = ten
        roomDepth = ten
        roomHeight = ten

        floor = box(pos=vector(0,-roomHeight/2,0),size=vector(roomWidth,wallThickness,roomDepth), color=color.white)
        ceiling = box(pos=vector(0,roomHeight/2,0),size=vector(roomWidth,wallThickness,roomDepth), color=color.white)
        backWall = box(pos=vector(0,0,-roomHeight/2),size=vector(roomWidth,roomHeight,wallThickness), color=color.white)
        leftWall = box(pos=vector(-roomHeight/2,0,0),size=vector(wallThickness,roomHeight,roomDepth), color=color.white)
        rightWall = box(pos=vector(roomHeight/2,0,0),size=vector(wallThickness,roomHeight,roomDepth), color=color.white)
        marble = sphere(radius=mRadius, color=color.red)
        deltaX = .1
        xPos= 0
        while True:
            rate(self.fps)
            xPos += deltaX
            if (xPos>roomWidth/2 or xPos < -(roomWidth/2)):
                deltaX = -deltaX
            marble.pos=vector(xPos,0,0)


if __name__ == "__main__":
    try:
        fps = int(input("How many FPS should I try to run at? (must be int): ")) if not test_path else fps
    except:
        fps = 60
        print(f"There was an error with your FPS input (wrong input type?), so I will just use {fps} FPS, GLFH :D")
    
    HyperComplex = SuperAwesomeAndComplexTree()
    SimpleTree = MehTree()
    HyperComplex.super_tree()
    
    if not test_path: input("\nDid you like it? I guess it missed some lights and decoration, let's do this again...")

    SimpleTree.learning_vpython()
    # I don't wanna go, Mr Stark
    while True: rate(10)