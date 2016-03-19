from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

x = -100
y = 13
z = -100

mc.player.setTilePos(x, y, z)
for i in range(1,100):
    mc.player.setTilePos(x+i, y, z+i)
    time.sleep(0.5)
