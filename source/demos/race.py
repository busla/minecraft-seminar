from mcpi.minecraft import Minecraft
from mcpi.vec3      import Vec3
from mcpi import block
import sys
import time 
from subprocess import *
import random

class Game(object):
    def __init__(self, mc, tokens, tile, burn):
        self.mc = mc
        self.tokens = tokens
        self.tile = tile
        self.burn = burn
        self.name = input('Hvað heitiru?: ')
        self.is_server = input('Ertu server? (j/n): ')        
        self.mc.postToChat(self.get_ip_address())        
        

    def get_ip_address(self):
        interface = 'wlan0'
        cmd = "ip -4 addr show "+interface+" | grep inet | awk '{print $2}' | cut -d/ -f1"

        p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
        output = p.communicate()[0]

        if p.returncode != 0:
            return None
        return output.decode()
    
            
    def round_vec3(self, vec3):
        return Vec3(int(vec3.x), int(vec3.y), int(vec3.z))

    def block_exists(self, vec3, block_list):
        for i in block_list:
            if (i.x == vec3.x) and (i.y == vec3.y) and (i.z == vec3.z):
                return True
        return False
    
    def play(self):

        self.reset_players()

        if self.is_server == 'j':
            self.set_tokens(self.tokens)            
            self.save_checkpoint()
            start = input('Ýttu á ENTER til að byrja: ')    
            self.mc.postToChat('BYRJA!!')
        total = 0
        block_list = []
        
        while True:
                    
            hits = self.mc.events.pollBlockHits()                    
            if len(hits) > 0:
                
                block_pos = self.round_vec3(Vec3(hits[0].pos.x, hits[0].pos.y, hits[0].pos.z))        
                block_type = self.mc.getBlock(block_pos)       
                                
                if block_type == self.tile: # and not self.block_exists(block_pos, block_list):
                    self.mc.setBlock(block_pos, self.burn)
                    total += len(hits)
                    self.mc.postToChat(self.name + ': ' + str(total))
                    if total >= 10:
                        self.mc.postToChat('Sigurvegari: '+self.name)
                        #sys.exit(0)
                        break
                block_list.append(block_pos)
            time.sleep(0.3)        
        
        restore = input('Ýttu á ENTER til að hreinsa kortið: ')
        game.restore_checkpoint()
        
        pass

    def reset_players(self):
        self.mc.postToChat('Nyr leikur ad hefjast ...')
        self.mc.player.setPos(0, 50, 0)
        pass

    def winner(self):
        pass

    def teleport(self):
        pass

    def set_tokens(self, tokens):
        coord = list(range(-90, 90))
        
        for i in range(0, tokens):
            self.mc.setBlock(random.choice(coord), random.choice(list(range(0, 10))), random.choice(coord), self.tile)

    def save_checkpoint(self):
        self.mc.saveCheckpoint()

    def restore_checkpoint(self):
        self.mc.restoreCheckpoint()
        self.play()

class World(object):
    def __init__(self, mc):
        self.mc = mc
        self.mc.postToChat('Undirby kortid ...')
        
    def clear_world(self):
        pass

    def build_world(self):
        pass

    def make_immutable(self):
        pass


mc = Minecraft.create()
game = Game(mc, tokens=1000, tile=22, burn=49)
game.play()




