from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()
  
while True:
    tile_pos = mc.player.getTilePos()
    tile_type = mc.getBlock(tile_pos)
    if tile_type is 0:
        mc.setBlock(tile_pos, 41)
    print(tile_type)
    time.sleep(0.1)    
