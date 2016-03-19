from mcpi.minecraft import Minecraft
import hashlib
import time
import sys
from mcpi.vec3 import Vec3

nafn = 'Jon'
mc = Minecraft.create()
total = 0
block_list = []
block_dict = {}
block_dict2 = {}

def round_vec3(vec3):
    return Vec3(int(vec3.x), int(vec3.y), int(vec3.z))

while True:
            
    hits = mc.events.pollBlockHits()
            
            
    if len(hits) > 0:
        block_dict['x'] = hits[0].pos.x
        block_dict['y'] = hits[0].pos.y
        block_dict['z'] = hits[0].pos.z

        block_dict2['x'] = hits[0].pos.x
        block_dict2['y'] = hits[0].pos.y
        block_dict2['z'] = hits[0].pos.z

        print(block_dict == block_dict2)                
        block_pos = round_vec3(Vec3(hits[0].pos.x, hits[0].pos.y, hits[0].pos.z))
        block_type = mc.getBlock(block_pos)
        print('block type: ', block_type)
        print(hits)
        
        
      
                        
        if block_dict not in block_list and block_type == 22:
            print('hits: ', hits)
            print('block pos: ', block_dict)
            
            block_list.append(block_dict)
            print('block list: ', block_list)
            total += len(hits)
            print('total: ', total)
                    
            if total >= 10:
                mc.postToChat('Sigurvegari: '+nafn)
                sys.exit(0)
    time.sleep(1)
