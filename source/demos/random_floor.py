from mcpi.minecraft import Minecraft
import time
import random

mc = Minecraft.create()

def render_tiles(pos, tiles, width, length):
    width = int(width / 2)
    length = int(length / 2)
    x_tiles = list(range(pos.x - length, pos.x + length))
    z_tiles = list(range(pos.z - width, pos.z + width))
    y = pos.y - 1
    
    for z in z_tiles:

        for x in x_tiles:
            mc.setBlock(x, y, z, random.choice(tiles))

        
    #mc.setBlock(x, pos.y, pos.z, tile)
        
while True:
    TILES = [5, 14, 16, 20, 22, 35, 4, 46, 45, 49, 57, 73, 80, 103, 246, 247]
    WIDTH = 8
    LENGTH = 8
    tile_pos = mc.player.getTilePos()
    tile_type = mc.getBlock(tile_pos)
    render_tiles(tile_pos, TILES, WIDTH, LENGTH)
    #print(tile_type)
    time.sleep(0.3)    
