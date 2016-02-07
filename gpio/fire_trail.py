from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

TORCH = 50
FIRE  = 51
LAVA_FLOWING = 10

while True:
    player_pos = mc.player.getTilePos()
    sleep(0.2)
    if mc.player.getTilePos() is not player_pos:
        mc.setBlock(player_pos, TORCH)

