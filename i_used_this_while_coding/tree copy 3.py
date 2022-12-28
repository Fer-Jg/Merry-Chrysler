from vpython import *

from re import sub as regex_change
from re import search as regex_find
from re import DOTALL as DoItCool
from time import sleep
from tkinter import Tk

from os import getcwd as mypath

# I don't want to input my FPS every time I test my program so I do this for later use (:
test_path = mypath().lower().startswith("C:\\Users\\inicio".lower())
fps = 60

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
        origin_w = int(self.get_curr_screen_geometry().split("x")[0])
        origin_h = int(self.get_curr_screen_geometry().split("x")[1].split("+")[0])
        w = origin_w * 0.60
        h = origin_h * 0.60
        print(f"Working with canvas size: {origin_w} x 0.60={w}, {origin_h} x 0.60={h}")
        self.scene = canvas(width=w, height=h,background=color.black, 
        # I  just want to have my own style for the site, the default one looked awful lol
        center=vector(0,0,0), ambient=color.black, title=f'''
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
        point_size = 10
        x_arrow = arrow(pos=vector(0,0,0), round=True, axis=vector(point_size,0,0), shaftwidth=1, color=color.red)
        y_arrow = arrow(pos=vector(0,0,0), round=True, axis=vector(0,point_size,0), shaftwidth=1, color=color.green)
        z_arrow = arrow(pos=vector(0,0,0), round=True, axis=vector(0,0,point_size), shaftwidth=1, color=color.blue)

    def new_learn(self):
        anyThick = 0.1
        # floor = box(pos=vector(0,0,0), size=vector(10,10,anyThick), color=vec(1,1,0))
        self.make_coords()
        while True:
            rate(fps)

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