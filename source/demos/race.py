from mcpi.minecraft import Minecraft
from mcpi.vec3      import Vec3
import sys
import time 
from mcpi import block

import random

class Game(object):
    def __init__(self, mc, tokens):
        self.mc = mc
        self.tokens = tokens
        self.mc.postToChat('Preparing race')
        
        
    def play(self):
        self.reset_players()
        self.set_tokens(self.tokens)
        self.save_checkpoint()        
        self.mc.postToChat('Race has started!')
        total = 0
        block_list = []
        while True:
            
            hits = self.mc.events.pollBlockHits()
            
            
            if len(hits) > 0:
                block_pos = Vec3(hits[0].pos.x, hits[0].pos.y, hits[0].pos.z)
                block_type = self.mc.getBlock(block_pos)
                if block_pos not in block_list and block_type == 1:
                    block_list.append(block_pos)
                    total += len(hits)
                    print(total)
                    
                    if total >= 10:
                        self.mc.postToChat('Thu vannst, jibbbi!!')
                        sys.exit(0)
            time.sleep(1)
        
        restore = input('Press ENTER to restore checkpoint')
        game.restore_checkpoint()
        
        pass

    def reset_players(self):
        self.mc.postToChat('Setting players to the starting point')
        self.mc.player.setPos(90, 18, -127)
        pass

    def winner(self):
        pass

    def teleport(self):
        pass

    def set_tokens(self, tokens):
        coord = list(range(-127, 127))
        
        for i in range(0, tokens):
            self.mc.setBlock(random.choice(coord), random.choice(list(range(0, 10))), random.choice(coord), 22)

    def save_checkpoint(self):
        self.mc.saveCheckpoint()

    def restore_checkpoint(self):
        self.mc.restoreCheckpoint()
        self.play()

class World(object):
    def __init__(self, mc):
        self.mc = mc
        self.mc.postToChat('Preparing world')
        
    def clear_world(self):
        pass

    def build_world(self):
        pass

    def make_immutable(self):
        pass


mc = Minecraft.create()

game = Game(mc, tokens=1000)
game.play()




