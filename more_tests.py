import ursina
import asyncio


# def update():
#     cone.rotation_y = cone.rotation_y #+ ursina.time.dt*100

def make_ursina_arrows(self):
    arrow_x = ursina.Entity(model="arrow", color=ursina.color.red, x=0.5)
    arrow_y = ursina.Entity(model="arrow", color=ursina.color.blue, rotation_z=-90, y=0.5)
    arrow_z = ursina.Entity(model="arrow", color=ursina.color.green, rotation_y=90, z=-0.5)
def tree_cone(self, rad : float, y : int = 0):
    return ursina.Entity(model=ursina.Cone(resolution=100, height=rad*1.5, radius=rad), color=ursina.color.white, y=y)

async def ursina_tree(self):
    global tree_levels
    global app
    app = ursina.Ursina()

    make_ursina_arrows(0)
    log = ursina.Entity(model=ursina.Cylinder(resolution=8, radius=.5, start=0, height=1, direction=(0,1,0), mode='triangle'#)) I tested and fixed a bug in ursina's repo while doing this part LOL
    , color_gradient=[ursina.color.white,ursina.color.white]))

    tree_bot = 0
    new_y = 30
    base_size = 0.5
    reduction_cons = 1
    tree_levels = []
    while new_y >= tree_bot:
        tree_levels.append(tree_cone(0, base_size, new_y))
        new_y = new_y - base_size
        base_size = base_size + reduction_cons

    ed = ursina.EditorCamera()
    app.run()

asyncio.run(ursina_tree(0))
#terrain_from_heightmap_texture = ursina.Entity(model=ursina.Terrain('heightmap_1', skip=8), scale=(40,5,20), texture='heightmap_1')


# light = ursina.PointLight(y=-20,color=ursina.color.green)
# light2 = ursina.duplicate(light, y=20, color=ursina.color.red)
