from mcpi.minecraft import Minecraft
import RPi.GPIO as virar
from mcpi.vec3 import Vec3
import random
import time

virar.setmode(virar.BCM)
virar.setup(21, virar.OUT)

mc = Minecraft.create()
teljari = 0

def round_vec3(vec3):
    return Vec3(int(vec3.x), int(vec3.y), int(vec3.z))


def render_tiles(pos, tile, width, length):
    width = int(width / 2)
    length = int(length / 2)
    x_tiles = list(range(pos.x - length, pos.x + length))
    z_tiles = list(range(pos.z - width, pos.z + width))
    y_tiles = list(range(pos.y - 5, pos.y))
    
    for z in z_tiles:
        for x in x_tiles:
            for y in y_tiles:
                  blokk = mc.getBlock(x, y, z)
                  if blokk == 247:                  
                        virar.output(21, virar.HIGH)
                        print("Fann blokk: %s" % random.random())
                        time.sleep(2)
                        virar.output(21, virar.LOW)
                        return
                  #print('Fann ekki blokk')

        
    #mc.setBlock(x, pos.y, pos.z, tile)


player_pos = mc.player.getPos()
random_block_pos = round_vec3(player_pos)
    
random_block_pos.x = random.randrange(random_block_pos.x - 50, random_block_pos.x + 50)
random_block_pos.y = random.randrange(random_block_pos.y - 5, random_block_pos.y + 10)
random_block_pos.z = random.randrange(random_block_pos.z - 50, random_block_pos.z + 50)

print(random_block_pos)
mc.setBlock(random_block_pos, 247)

while True:
    GOLD = 41
    WIDTH = 6
    LENGTH = 6
    tile_pos = mc.player.getTilePos()
    #tile_type = mc.getBlock(tile_pos)
    render_tiles(tile_pos, GOLD, WIDTH, LENGTH)
    #print(tile_type)
    time.sleep(1) 
"""
while True:
      steve = mc.player.getTilePos()
      blokk = mc.getBlock(steve.x, steve.y-1, steve.z)
      
      if blokk == 2:                  
            virar.output(21, virar.HIGH)
            mc.postToChat("Fann gras")
            time.sleep(2)
            virar.output(21, virar.LOW)
      
            
"""
