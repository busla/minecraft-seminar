from mcpi.minecraft import Minecraft

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
        restore = input('Press ENTER to restore checkpoint')
        game.restore_checkpoint()
        
        pass

    def reset_players(self):
        self.mc.postToChat('Setting players to the starting point')
        self.mc.player.setPos(127, 0, 127)
        pass

    def winner(self):
        pass

    def teleport(self):
        pass

    def set_tokens(self, tokens):
        coord = list(range(-127, 127))
        
        for i in range(0, tokens):
            self.mc.setBlock(random.choice(coord), random.choice(list(range(0, 10))), random.choice(coord), block.LAPIS_LAZULI_BLOCK)

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




