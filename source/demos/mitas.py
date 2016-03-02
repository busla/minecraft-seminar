from mcpi.minecraft import Minecraft, Vec3
import time

mc = Minecraft.create()
is_rendering = False

def render_tiles(pos, tile, width, length):
    
    width = int(width / 2)
    length = int(length / 2)
    x_tiles = list(range(pos.x - length, pos.x + length))
    z_tiles = list(range(pos.z - width, pos.z + width))
    y_tiles = list(range(pos.y - width, pos.y + width))
    #y = pos.y - 1
    
    for z in z_tiles:
        for x in x_tiles:
            for y in y_tiles:
                if not mc.getBlock(x, y, z) == 0:
                    mc.setBlock(x, y, z, tile)



while True:
    hits = mc.events.pollBlockHits()
    print(hits)
    if len(hits) > 0:
            
        x, y, z = hits[0].pos.x, hits[0].pos.y, hits[0].pos.z
        vec = Vec3(x, y, z)
        render_tiles(vec, 41, 10, 10)
        mc.events.clearAll()

        
        #print(mc.getBlockWithData(x, y, z))        
        #mc.setBlock(x, y, z, 41)
            
    time.sleep(0.1)
