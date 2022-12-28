from tree import Utils
import random


from typing import List
import ursina as u
from ursina.shaders import lit_with_shadows_shader
import asyncio

global items
global g_lights
global g_spheres
items = []
g_lights = []
g_spheres = []
counter = 0
def update():
    global counter
    counter +=1
    random.choice(g_lights).scale = 0 + 4 * u.sin(counter * 0.005)
    random.choice(g_spheres).scale = 0 + 1 * u.sin(counter * 0.005)

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

colors = myColors()

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
    global tree_levels
    global app
    global curve_res
    curve_res = 400
    app = u.Ursina()

    make_ursina_arrows(0)
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
        temp_cone = tree_cone(0, rad=base_size, y=new_y)
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
                sfir = chrimu_sfir(0, pos=[x,l.y,z], color = sph_color)
                sfir.rad = 1
                g_lights.append(lait)
                g_spheres.append(sfir)

    # Real Scene
    ground = u.Entity(model='plane', scale=64, texture='grass', color=u.color.gray, texture_scale=(32,32), collider='box', shader=lit_with_shadows_shader)
    # sky = u.Sky(texture="sky_sunset")
    ed = u.EditorCamera()
    ed.y = ed.y+10
    # ed.z = ed.z-200
    app.run()


asyncio.run(ursina_tree(0))
#terrain_from_heightmap_texture = u.Entity(model=u.Terrain('heightmap_1', skip=8), scale=(40,5,20), texture='heightmap_1')


# light = u.PointLight(y=-20,color=u.color.green)
# light2 = u.duplicate(light, y=20, color=u.color.red)
