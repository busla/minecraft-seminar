from mcpi.minecraft import Minecraft
import time
import random

mc = Minecraft.create()

def render_tiles(pos, tile, width, length):
    width = int(width / 2)
    length = int(length / 2)
    x_tiles = list(range(pos.x - length, pos.x + length))
    z_tiles = list(range(pos.z - width, pos.z + width))
    y = pos.y - 1
    
    for z in z_tiles:

        for x in x_tiles:
            mc.setBlock(x, y, z, tile)

        
    #mc.setBlock(x, pos.y, pos.z, tile)
TILES = [41, 20]
tile_index = 0        
last_tile = len(TILES) -1

while True:

    if not tile_index == last_tile:
        tile_index += 1
    else:
        tile_index = 0

    WIDTH = 8
    LENGTH = 8
    tile_pos = mc.player.getTilePos()
    tile_type = mc.getBlock(tile_pos)
    render_tiles(tile_pos, TILES[tile_index], WIDTH, LENGTH)
    #print(tile_type)
    time.sleep(0.3)    
