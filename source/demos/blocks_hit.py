from mcpi.minecraft import Minecraft
import hashlib
import time
import sys
from mcpi.vec3 import Vec3

def round_vec3(vec3):
    return Vec3(int(vec3.x), int(vec3.y), int(vec3.z))

def block_exists(vec3, block_list):
    for i in block_list:
        if (i.x == vec3.x) and (i.y == vec3.y) and (i.z == vec3.z):
            return True
    return False

def start():
    total = 0
    block_list = []
    
    while True:
                
        hits = mc.events.pollBlockHits()
                
                
        if len(hits) > 0:
            
            block_pos = round_vec3(Vec3(hits[0].pos.x, hits[0].pos.y, hits[0].pos.z))        
            block_type = mc.getBlock(block_pos)       
                            
            if block_type == TILE and not block_exists(block_pos, block_list):
                mc.setBlock(block_pos, 0)
                total += len(hits)
                print('total: ', total)
                mc.postToChat(nafn + ': ' + str(total))
                if total >= 10:
                    mc.postToChat('Sigurvegari: '+nafn)
                    #sys.exit(0)
                    return
            block_list.append(block_pos)
        time.sleep(1)

mc = Minecraft.create()

nafn = input('Hvað heitiru?: ')
TILE = 5
mc.player.setPos(0,20,0)

while True:
    mc.postToChat(nafn + ' er komin/n')
    start()
    input('Ýttu á ENTER til að byrja aftur: ')
