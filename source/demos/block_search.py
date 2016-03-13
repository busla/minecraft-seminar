from mcpi.minecraft import Minecraft
import RPi.GPIO as virar

import time

virar.setmode(virar.BCM)
virar.setup(21, virar.OUT)

mc = Minecraft.create()

teljari = 0


while True:
      steve = mc.player.getTilePos()
      blokk = mc.getBlock(steve.x, steve.y-1, steve.z)
      
      if blokk == 2:                  
            virar.output(21, virar.HIGH)
            mc.postToChat("Fann gras")
            time.sleep(2)
            virar.output(21, virar.LOW)
      
            
