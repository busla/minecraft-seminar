from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

while True:

    hits = mc.events.pollBlockHits()
    
    if len(hits) > 0:
        x, y, z = hits[0].pos.x, hits[0].pos.y, hits[0].pos.z
        
        mc.setBlock(x, y, z, 41)
        
    time.sleep(0.1)
