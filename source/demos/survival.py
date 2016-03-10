from mcpi.minecraft import Minecraft, Vec3
from mcpi import block

from clear_world import clear_world
import random

mc = Minecraft.create()

def render_tiles(pos_start, pos_end, tiles):
    
    x_tiles = list(range(pos_start.x, pos_end.x))
    z_tiles = list(range(pos_start.z, pos_end.z))
    y_tiles = list(range(pos_start.y, pos_end.y))
    
    for z in z_tiles:
        for x in x_tiles:
            for y in y_tiles:
                random_block = random.choice(tiles)
                mc.setBlock(x, y, z, random_block)
                

        
    
start = -128
end = 128

# Vec3() býr hlut með hnitum
world_start = Vec3(start, 0, start)
world_end = Vec3(end, 11, end)

roof_start = Vec3(start, 11, start)
roof_end = Vec3(start, 12, start)

clear_world(roof_start, roof_end, block.STONE)
render_tiles(world_start, world_end, [0, 0, 0, 4])
    
