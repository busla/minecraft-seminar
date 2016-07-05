from mcpi.minecraft import Minecraft
import time

tenging = Minecraft.create()

while 1+1 == 2:
    steve = tenging.player.getTilePos()
    print(steve)
    time.sleep(0.1)
    #tenging.setBlock(steve, 73)
    tenging.setBlock((steve.x, steve.y, steve.z), 73)
