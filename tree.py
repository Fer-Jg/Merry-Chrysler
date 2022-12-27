from vpython import *

import random
import math
from re import sub as regex_change
from re import search as regex_find
from re import DOTALL as DoItCool
from time import sleep
from tkinter import Tk
from os import getcwd as mypath


import asyncio
from typing import List
import ursina as u
from ursina.shaders import lit_with_shadows_shader

# I don't want to input my FPS every time I test my program so I do this for later use (:
test_path = mypath().lower().startswith("C:\\Users\\inicio".lower())
fps = 60

global step
global items
global g_lights
global g_spheres
global counter
step = 0
items = []
g_lights = []
g_spheres = []
counter = 0


class myColors():
    black = u.color.black
    brown_likea_tree = u.color.rgb(118,92,72)
    dark_chrimu_green = u.color.rgb(0, 102, 0)
    light_chrimu_green = u.color.rgb(5, 96, 15)
    chrimu_red = u.color.rgb(193, 12, 3)
    chrimu_blue = u.color.rgb(37, 92, 182)
    chrimu_purple = u.color.rgb(163, 54, 198)
    chrimu_oranga = u.color.rgb(203, 94, 1)
    chrimu_silver = u.color.rgb(199, 199, 199)
    chrimu_gold = u.color.rgb(208, 179, 48)
    chrimu_magenta = u.color.rgb(203, 8, 152)

    merry_chrisis_sphere_choices = [light_chrimu_green,chrimu_red,chrimu_blue,chrimu_purple,chrimu_oranga,chrimu_silver,chrimu_gold,chrimu_magenta]
    
    angy_red = u.color.red

global colors
colors = myColors()

class Utils():

    @staticmethod
    def circle_coords(origin_x:int, origin_y:int, radius:int, stepSize:float = 0.1):
        positions = []
        t = 0
        while t < 2 * math.pi:
            positions.append((radius * math.cos(t) + origin_x, radius * math.sin(t) + origin_y))
            t += stepSize
        return positions

class SuperAwesomeAndComplexTree():
    def make_tree(self, tab : int = 10) -> str:
        built_tree = ""
        # Leaves and branches and those pointy thingies, basically the top of the tree
        for x in range(tab): built_tree += " "*(tab-x) + "*"*(x) + "*"*(x-1) + "\n"
        # Log, trunk, idk what was the word in english lol
        for x in range(int(tab/4)): built_tree += " "*(tab-1) + "*\n"
        # Print the whole super cool and complex tree...
        return built_tree

    def print_tree(self, tab : int = 10) -> None:
        to_print = self.make_tree()
        for x in to_print:
            print(x, end="")
            sleep(((1/1)/(fps if fps > 100 else 100)) if not test_path else 0)


class MehTree():

    def get_curr_screen_geometry(self):
        """
        Workaround to get the size of the current screen in a multi-screen setup.
        Returns:
            geometry (str): The standard Tk geometry string.
                [width]x[height]+[left]+[top]

        Source: https://stackoverflow.com/questions/3129322/how-do-i-get-monitor-resolution-in-python/56913005#56913005
        """
        root = Tk()
        root.update_idletasks()
        root.attributes('-fullscreen', True)
        root.state('iconic')
        geometry = root.winfo_geometry()
        root.destroy()
        return geometry
        
    def __init__(self) -> None:
        self.ursina = False
        origin_w = int(self.get_curr_screen_geometry().split("x")[0])
        origin_h = int(self.get_curr_screen_geometry().split("x")[1].split("+")[0])
        w = origin_w * 0.60
        h = origin_h * 0.60
        print(f"Working with canvas size: {origin_w} x 0.60={w}, {origin_h} x 0.60={h}")
        self.scene = canvas(width=w, height=h,background=color.black, 
        # I  just want to have my own style for the site, the default one looked awful lol
        center=vector(0,10,0), ambient=color.black, title=f'''
        <div class="title"><h1 class="title">Merry Christmas, Pythonistas!</h1></div>
        <script>
        function changeFavicon(src) {{
        var link = document.createElement('link'),
            oldLink = document.getElementById('dynamic-favicon');
            link.id = 'dynamic-favicon';
            link.rel = 'shortcut icon';
            link.href = src;
            if (oldLink) {{
            document.head.removeChild(oldLink);
            }}
            document.head.appendChild(link);
            }}
        changeFavicon('https://cdn3d.iconscout.com/3d/premium/thumb/python-6815592-5602757.png');
        document.title= "Pythonistree!";
        </script>
        <style>
			:root{{
			    --chrs-black: #190508;
			    --chrs-dark-coffee: #4F100E;
			    --chrs-light-coffee: #7F1813;
			    --chrs-red: #CB2924;
			    --green-yellow: #9AD658;
			    --chrs-greeny: #236644;
			}}
			body {{
			    background-color:var(--chrs-red);
			}}
			div.title {{
			    width: {w};
			    height: inherit;
			}}
			h1.title {{
			    font-weight: 900;
			    color: var(--chrs-greeny);
			    text-decoration-color: var(--chrs-greeny);
			}}
		</style>
        ''',
        caption='''
        <div class="caption"><h1 class="caption">And Happy New Year!! 😄</h1></div>
        ''')
        scene.lights = []
        self.scene.lights = []
        self.scene.up = vector(0, 1, 0)
        #print(self.scene.camera.axis) # Maybe change this later?
        self.scene.camera.pos = vector(0, 10, 0)

    def old_title(self) -> str:
        match = regex_find(r'<h1 class="title">(.*?)</h1>', self.scene.title, flags=DoItCool)
        #print(f"Found old title: {match.group(1)}")
        return match.group(1)

    def change_title(self, new_title : str):
        new_text = regex_change(r'<h1 class="title">.*</h1>', f'<h1 class="title">{new_title}</h1>', self.scene.title, flags=DoItCool)
        self.scene.title = new_text

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
        scene.camera.pos = vector(10,10,10)
        scene.camera.axis = vector(0,0,0)
        marble = sphere(radius=mRadius, color=color.red)
        deltaX = .1
        xPos= 0
        titled = False
        while True:
            rate(fps)
            xPos += deltaX
            if (xPos>roomWidth/2 or xPos < -(roomWidth/2)):
                deltaX = -deltaX
            marble.pos=vector(xPos,0,0)

            if not titled:
                self.change_title(self.old_title().replace(self.old_title(),"Hi hi"))
                titled = True
    
    def make_coords(self):
        point_size = 15
        x_arrow = arrow(pos=vector(0,0,0), round=True, axis=vector(point_size,0,0), shaftwidth=0.25, color=color.red)
        y_arrow = arrow(pos=vector(0,0,0), round=True, axis=vector(0,point_size,0), shaftwidth=0.25, color=color.green)
        z_arrow = arrow(pos=vector(0,0,0), round=True, axis=vector(0,0,point_size), shaftwidth=0.25, color=color.blue)
        coords_label = label(pos=x_arrow.pos, height=16, border=4, xoffset=15, yoffset=15, text="XYZ", font="sans")

        #self.scene.forward = vector(-1, -1, -1)
    
    def make_star(self):
        st = shapes.star()
        star_0 = extrusion(path=[vec(0,22,-.125), vec(0,22,.125)], shape=st, scale=2, color=color.yellow, emissive=True)
        star_45 = star_0.clone().rotate(angle=pi/4, axis=vector(0,22,0))
        star_45_ = star_0.clone().rotate(angle=-pi/4, axis=vector(0,22,0))
        star_90 = star_0.clone().rotate(angle=pi/2, axis=vector(0,22,0))

        star_light = local_light(pos=vector(star_0.pos.x,star_0.pos.y+1,star_0.pos.z), color=color.yellow)

    def new_learn(self):
        self.make_star()
        tree_components = []
        log_top = 20

        base = box(pos=vector(0,0,0), size=vector(5, 0.1, 5),  shininess=0.4, texture=textures.wood)
        log = cylinder(pos=vector(0,0,0), axis=vector(0,log_top,0),texture=textures.wood_old, radius=0.5, shininess=0.2)

        green_like_tree = vector(0,0.5,0)
        tree_levels = []
        new_pos = 5
        conv_const = 0.5
        rad = 6
        while new_pos + rad <= log_top+2:
            tree_components.append(cone(pos=vector(0,new_pos,0), axis=vector(0,rad,0), radius=rad-(conv_const), color=green_like_tree))
            tree_levels.append({"vector": vector(0,new_pos,0), "radius": rad-(conv_const)})
            new_pos += 2
            rad = rad-(conv_const)
        tree_compound = compound(tree_components)
        light_colors = [color.yellow, color.red, color.blue, color.orange, color.green]
        light_levels = []
        dot_levels = []
        for w in range(4):
            for i, level in enumerate(tree_levels):
                pos_x = level.get("vector").x
                pos_y = level.get("vector").y
                pos_z = level.get("vector").z
                rad = level.get("radius")
                coords_list = Utils.circle_coords(pos_x, pos_z, rad, 0.55)
                limit = (len(coords_list)-1)
                def delimit(val : int) -> int:
                    return val if val < limit else val-limit
                poper = (delimit(int(len(coords_list)/3)+i) 
                # Just want to point out the "in [whatever]" was for something I thought before but meh, I'll leave it like that
                        if w in [0,3] else delimit(2*int(len(coords_list)/3)+i) 
                        if w in [1,4] else delimit(3*int(len(coords_list)/3)+i))
                # print(f"Pos {i},{w} : {limit} - {poper}") 
                x , z = coords_list[poper]
                set_color = random.choice(light_colors)
                nlight = local_light(pos=vector(x,pos_y,z), color=set_color, visible=(i+w)%2==0)
                light_levels.append(nlight)
                ndot = points(pos=[vector(x,pos_y,z)], radius=0.3, size_units="world", color=set_color)
                dot_levels.append(ndot)
        itera = 0
        ursined = False
        while True:
            rate(fps)
            # scene.pause()
            light_levels[itera].visible = not light_levels[itera].visible
            dot_levels[itera].modify(0,visible = not dot_levels[itera].visible)
            print(light_levels[itera].visible)
            itera = itera+1 if itera+1 < len(light_levels)-1 else 0
            # scene.pause()
            input("Done? Press enter")
            if not ursined:
                ursined = True
                asyncio.run(self.ursina_tree())

    async def ursina_tree(self):
        app = ursina.Ursina()
        cone = ursina.Entity(model=ursina.Cone(), color=ursina.color.green)
        ed = ursina.EditorCamera()
        app.run()


if __name__ == "__main__":
    try:
        fps = int(input("How many FPS should I try to run at? (must be int): ")) if not test_path else fps
    except:
        fps = 60
        print(f"There was an error with your FPS input (wrong input type?), so I will just use {fps} FPS, GLFH :D")
    
    HyperComplex = SuperAwesomeAndComplexTree()
    SimpleTree = MehTree()
    HyperComplex.make_tree()
    
    if not test_path: input("\nDid you like it? I guess it missed some lights and decoration, let's do this again...")

    SimpleTree.new_learn()

    # I don't wanna go, Mr Stark
    while True: rate(10)