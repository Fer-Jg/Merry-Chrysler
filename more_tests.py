from tree import Utils
import random


from typing import List
import ursina as u
import asyncio


# def update():
#     cone.rotation_y = cone.rotation_y #+ u.time.dt*100

class myColors():
    black = u.color.black
    brown_likea_tree = u.color.rgb(118,92,72)
    chrimu_green = u.color.rgb(35, 102, 68)
    chrimu_red = u.color.rgb(195, 15, 22)
    chrimu_blue = u.color.rgb(31, 39, 102)
    angy_red = u.color.red

colors = myColors()

def make_ursina_arrows(self):
    arrow_x = u.Entity(model="arrow", color=u.color.red, x=0.5)
    arrow_y = u.Entity(model="arrow", color=u.color.blue, rotation_z=-90, y=0.5)
    arrow_z = u.Entity(model="arrow", color=u.color.green, rotation_y=90, z=-0.5)

def tree_cone(self, rad : float, y : int = 0):
    return u.Entity(model=u.Cone(resolution=curve_res, height=rad*1.5, radius=rad), color=colors.chrimu_green, y=y)

def chrimu_sfir(self, color = None, pos : List[int] = None):
    if pos:
        if len(pos) < 3: raise IndexError("`pos` arg is missing some coords, broudy")
        x = pos[0]
        y = pos[1]
        z = pos[2]
    else: x,y,z = 0,0,0
    return u.Entity(model="sphere", color=color if color else myColors.angy_red, x=x, y=y, z=z)


async def ursina_tree(self):
    global tree_levels
    global app
    global curve_res
    curve_res = 400
    app = u.Ursina()

    make_ursina_arrows(0)
    log = u.Entity(model=u.Cylinder(resolution=curve_res, radius=.5, start=0, height=5.6, direction=(0,1,0)#)) I tested and fixed a bug in ursina's repo while doing this part LOL
    , color_gradient=[colors.brown_likea_tree]))
    log_top = u.Entity(model=u.Cylinder(resolution=curve_res, radius=1, start=5.4, height=5.6, direction=(0,1,0), color_gradient=[colors.brown_likea_tree]))

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

    ed = ursina.EditorCamera()
    merry_chrisis_colors = [colors.chrimu_green, colors.chrimu_green, colors.chrimu_blue]
    if False:
        for w in range(1):
            for i, l in enumerate(tree_levels):
                circ = Utils.circle_coords(l.x,l.y,l.radius)
                limit = (len(circ)-1)
                def delimit(val : int) -> int:
                    return val if val < limit else val-limit
                poper = delimit(i)
                x, z = circ[poper]
                sph_color = random.choice(merry_chrisis_colors)
    ground = u.Entity(model='plane', scale=64, texture='white_cube', texture_scale=(32,32), collider='box')
    sky = u.Sky(texture="sky_sunset")
    ed = u.EditorCamera()
    ed.y = ed.y+10
    # ed.z = ed.z-200
    app.run()

asyncio.run(ursina_tree(0))
#terrain_from_heightmap_texture = u.Entity(model=u.Terrain('heightmap_1', skip=8), scale=(40,5,20), texture='heightmap_1')


# light = u.PointLight(y=-20,color=u.color.green)
# light2 = u.duplicate(light, y=20, color=u.color.red)
