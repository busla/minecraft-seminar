from mcpi.minecraft import Minecraft
import time

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
        
while True:
    GOLD = 41
    WIDTH = 8
    LENGTH = 8
    tile_pos = mc.player.getTilePos()
    #tile_type = mc.getBlock(tile_pos)
    render_tiles(tile_pos, GOLD, WIDTH, LENGTH)
    #print(tile_type)
    time.sleep(1)    
