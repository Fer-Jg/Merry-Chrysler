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


import subprocess
from os import path
from requests import get as gimmeMyRequest

# I don't want to input my FPS every time I test my program so I do this for later use (:
global test_path
test_path = mypath().lower().startswith("C:\\Users\\inicio".lower())
global fps
fps = 60

global res_w
global res_h

global step
global items
global app
global g_lights
global g_spheres
global counter

global icon_file
icon_file = "icon.ico"
global bg_music_name
global bg_music
bg_music_name = "Best_Chrimu_Song.mp3"
global ursified
ursified = False

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


# Ursina Stuff
# Ursina updates
def update():
    if ursified:
        global counter
        counter +=1
        random.choice(g_lights).scale = 0 + 4 * u.sin(counter * 0.005)
        random.choice(g_spheres).scale = 0 + 1 * u.sin(counter * 0.005)

def exCiting():
    print("Bye bye")

class UrsinaUltimateTree():
    def download_music(self):
        global bg_music_name
        bg_music_name = "Best_Chrimu_Song.mp3"
        
        download_stuff = not path.exists(bg_music_name)
        # If there is no mp3 file we should just avoid requests and other processes, right?
        print("Getting the most Chrismas-y song an AI could find...")
        if download_stuff:
            url = "https://cdn.trendybeatz.com/audio/Mariah-Carey-All-I-Want-For-Christmas-Is-You-(TrendyBeatz.com).mp3"
            download = gimmeMyRequest(url)
        
        # All utility names
        initial_output_name = "fix_" + bg_music_name.replace(".mp3",".wav")
        fixed_output_name = initial_output_name.replace("fix_","")
        bg_music_name = fixed_output_name

        # Actually download the song, but in a mp3 format, so let's fix that later...
        if download_stuff:
            with open(bg_music_name, "wb") as f:    f.write(download.content)

        # Make song a wav file
        subprocess.run(['ffmpeg', '-y', '-i', bg_music_name, initial_output_name], 
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        # Cut the wav file from the first 7.5 seconds because the download site has some annoying ad through that bit
        subprocess.run(['ffmpeg', '-y', '-i', initial_output_name, '-ss', '00:00:07.5', '-c', 'copy', fixed_output_name], 
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    def download_icon(self):
        download_stuff = not path.exists(icon_file)
        
        print("Getting icon file...")
        if download_stuff:
            url = "https://cdn3d.iconscout.com/3d/premium/thumb/python-6815592-5602757.png"
            req = gimmeMyRequest(url)
            with open(icon_file, "wb") as file:
                file.write(req.content)
        icoed_icon = icon_file.replace(".png",".ico")
        print(f"{icoed_icon} {not path.exists(icoed_icon)}")
        if not path.exists(icoed_icon):
            subprocess.run(['convert', icon_file, icoed_icon])

    def play_music(self):
        global bg_music_name
        global bg_music
        bg_music = u.Audio(
                bg_music_name,
                volume=.2,
                loop = True,
                autoplay = True,
                enabled = [])

    def setSystemIcon(self):
        self.download_icon()
        u.window.icon = icon_file


    def setAppData(self):
        self.download_music()
        self.setSystemIcon()
        u.window.title = "Pythonistree!"
        
    def __init__(self) -> None:
        global app

        self.setAppData()
        app = u.Ursina(development_mode=not test_path, fullscreen=False, borderless = False)
        u.window.exit_button.visible = True
        u.window.exit_button.on_click = exCiting

    def make_ursina_arrows(self):
        arrow_x = u.Entity(model="arrow", color=u.color.red, x=0.5)
        arrow_y = u.Entity(model="arrow", color=u.color.blue, rotation_z=-90, y=0.5)
        arrow_z = u.Entity(model="arrow", color=u.color.green, rotation_y=90, z=-0.5)

    def tree_cone(self, rad : float, y : int = 0):
        return u.Entity(model=u.Cone(resolution=curve_res, height=rad*1.5, radius=rad), color=colors.dark_chrimu_green, y=y, 
        texture="grass", shader=lit_with_shadows_shader)

    def chrimu_sfir(self, color = None, pos : List[int] = None, **kwargs):
        if pos:
            if len(pos) < 3: raise IndexError("`pos` arg is missing some coords, broudy")
            x = pos[0]
            y = pos[1]
            z = pos[2]
        else: x,y,z = 0,0,0
        return u.Entity(model="sphere", color=color if color else myColors.angy_red, x=x, y=y, z=z, alpha=.5,shader=lit_with_shadows_shader, **kwargs)


    async def ursina_tree(self):
        global test_path
        global step
        global tree_levels
        global app
        global curve_res
        curve_res = 400
        
        while step < 2: print("Waiting for step...")

        if test_path: self.make_ursina_arrows()
        log = u.Entity(model=u.Cylinder(resolution=curve_res, radius=.5, start=0, height=5.6, direction=(0,1,0)#)) I tested and fixed a bug in ursina's repo while doing this part LOL
        , color_gradient=[colors.brown_likea_tree]), shader=lit_with_shadows_shader)
        log_top = u.Entity(model=u.Cylinder(resolution=curve_res, radius=1, start=5.4, height=5.6, direction=(0,1,0)
        , color_gradient=[colors.brown_likea_tree]), shader=lit_with_shadows_shader)

        tree_bot = 0
        new_y = 30
        base_size = 0.5
        reduction_cons = 1
        tree_levels = []
        while new_y >= tree_bot:
            temp_cone = self.tree_cone(rad=base_size, y=new_y)
            temp_cone.radius = base_size
            temp_cone.rad = temp_cone.radius # in case i wanna call it this way, ok? ok
            tree_levels.append(temp_cone)
            new_y = new_y - base_size
            base_size = base_size + reduction_cons
        rounds = 8
        tree_levels.reverse()
        for w in range(rounds):
            for i, l in enumerate(tree_levels):
                if i>=len(tree_levels)-2: break
                circ = Utils.circle_coords(l.x,l.z,l.radius)
                limit = (len(circ)-1)
                followup = True
                if (i >= len(tree_levels)-3):
                    odds = [True]
                    for _a_ in (range(i-3) if i>3 else range(i)): odds.append(False)
                    # print(odds)
                    followup = random.choice(odds)
                if followup:
                    def delimit(val : int) -> int: return val if val < limit else val-limit
                    val = int(w*(limit/rounds))+((1+limit%20)*i)
                    poper = delimit(val)
                    x, z = circ[poper]
                    sph_color = random.choice(colors.merry_chrisis_sphere_choices)
                    # lait = u.PointLight(x=x,y=l.y, z=z, color = sph_color*.5,
                    # shadows=True)
                    lait = u.Entity(model='quad', texture='radial_gradient', x=x, y=l.y, z=z, 
                                    billboard=True, color=sph_color, render_queue=1, alpha=.5)
                    sfir = self.chrimu_sfir(pos=[x,l.y,z], color = sph_color)
                    sfir.rad = 1
                    g_lights.append(lait)
                    g_spheres.append(sfir)

        # Real Scene
        ground = u.Entity(model='plane', scale=64, texture='grass', color=u.color.gray, texture_scale=(32,32), collider='box', shader=lit_with_shadows_shader)
        # sky = u.Sky(texture="sky_sunset")
        ed = u.EditorCamera()
        ed.y = ed.y+10
        ed.z = ed.z-30
        ed.look_at(ground)
        # ed.z = ed.z-200
        self.play_music()
        app.run(info=False)



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
        
    def __init__(self, previous : UrsinaUltimateTree = None) -> None:
        global res_w
        global res_h
        self.ursina = False
        origin_w = int(self.get_curr_screen_geometry().split("x")[0])
        origin_h = int(self.get_curr_screen_geometry().split("x")[1].split("+")[0])
        res_w = origin_w * 0.60
        res_h = origin_h * 0.60
        print(f"Working with canvas size: W:({origin_w} x 0.60 = {res_w}) x H:({origin_h} x 0.60 = {res_h})")
        self.scene = canvas(width=res_w, height=res_h,background=color.black, 
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
			div.title, div.caption{{
			    width: {res_w};
			    height: inherit;
			}}
			h1.title, div.caption {{
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
    
    def make_star(self):
        st = shapes.star()
        star_0 = extrusion(path=[vec(0,22,-.125), vec(0,22,.125)], shape=st, scale=2, color=color.yellow, emissive=True)
        star_45 = star_0.clone().rotate(angle=pi/4, axis=vector(0,22,0))
        star_45_ = star_0.clone().rotate(angle=-pi/4, axis=vector(0,22,0))
        star_90 = star_0.clone().rotate(angle=pi/2, axis=vector(0,22,0))

        star_light = local_light(pos=vector(star_0.pos.x,star_0.pos.y+1,star_0.pos.z), color=color.yellow)

    async def vpy_tree(self):
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
        global step
        print("\n\nNow look at your web browser ;)")
        ursination = UrsinaUltimateTree()
        while True:
            rate(fps)
            # # scene.pause()
            # light_levels[itera].visible = not light_levels[itera].visible
            # dot_levels[itera].modify(0,visible = not dot_levels[itera].visible)
            # print(light_levels[itera].visible)
            # itera = itera+1 if itera+1 < len(light_levels)-1 else 0
            # # scene.pause()
            if step < 2:
                input("Done? Press enter")
                step = 2
                ursified = True
                await ursination.ursina_tree()

class SuperAwesomeAndComplexTree():

    def make_tree(self, previous : MehTree = None, tab : int = 10) -> str:
        built_tree = ""
        # Leaves and branches and those pointy thingies, basically the top of the tree
        for x in range(tab): built_tree += " "*(tab-x) + "*"*(x) + "*"*(x-1) + "\n"
        # Log, trunk, idk what was the word in english lol
        for x in range(int(tab/4)): built_tree += " "*(tab-1) + "*\n"
        # Print the whole super cool and complex tree...
        return built_tree

    def __init__(self, tab : int = 10) -> None:
        self.to_print = self.make_tree(tab)

    def print_tree(self) -> None:
        for x in self.to_print:
            print(x, end="")
            sleep(((1/1)/(fps if fps > 100 else 100)) if not test_path else 0)



async def run_tasks():
    await asyncio.gather(SimpleTree.vpy_tree(),
                        return_exceptions=True)

if __name__ == "__main__":
    try:
        fps = int(input("How many FPS should I try to run at? (must be int): ")) if not test_path else fps
    except:
        fps = 60
        print(f"There was an error with your FPS input (wrong input type?), so I will just use {fps} FPS, GLFH :D")
    
    HyperComplex = SuperAwesomeAndComplexTree()
    SimpleTree = MehTree()
    HyperComplex.make_tree()

    if not test_path:
        HyperComplex.print_tree()
        input("\nDid you like it? I guess it missed some lights and decoration, let's do this again...")

    asyncio.run(run_tasks())

    # I don't wanna go, Mr Stark
    while True: rate(10)