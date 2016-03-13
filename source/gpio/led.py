import RPi.GPIO as GPIO
from time import sleep
from mcpi.minecraft import Minecraft, Vec3
import mcpi.block as block

import random
import math


GPIO.setwarnings(False)

PIN = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)



def led_off():
    GPIO.output(PIN, GPIO.LOW)
    
def led_on():   
    GPIO.output(PIN, GPIO.HIGH)

def led_blink(speed):
        led_on()
        sleep(speed)
        led_off()
        sleep(speed)

    
def round_vec3(vec3):
    return Vec3(int(vec3.x), int(vec3.y), int(vec3.z))

def distance_between_points(point1, point2):
    xd = point2.x - point1.x
    yd = point2.y - point1.y
    zd = point2.z - point1.z
    return math.sqrt((xd*xd) + (yd*yd) + (zd*zd))

if __name__ == "__main__":
    mc = Minecraft.create()
    mc.postToChat("VELKOMIN!...")
    
    sleep(2)

    mc.player.setPos(1,mc.getHeight(1,1),1)
    player_pos = mc.player.getPos()
    print('Þú ert á hniti: %s' % player_pos)
    
    random_block_pos = round_vec3(player_pos)
    
    random_block_pos.x = random.randrange(random_block_pos.x - 50, random_block_pos.x + 50)
    #random_block_pos.y = random.randrange(random_block_pos.y - 10, random_block_pos.y + 10)
    random_block_pos.z = random.randrange(random_block_pos.z - 50, random_block_pos.z + 50)
    print(random_block_pos)
    mc.setBlock(random_block_pos, 246)  
    
    #mc.setBlock(treasure)
    seeking = True
    last_player_pos = player_pos
    last_distance_from_block = distance_between_points(random_block_pos, last_player_pos)
    print(last_distance_from_block)
    position = 5

    

    while (seeking == True):
        player_pos = mc.player.getPos()
        
        if last_player_pos != player_pos:
            distance_from_block = distance_between_points(random_block_pos, player_pos)
            #print("Distance: %s" % distance_from_block)
        
            if distance_from_block < 2:
                # found block
                seeking = False
                
            else:
                if distance_from_block <= 5:
                    led_on()

                if 6 < distance_from_block <= 11:
                    led_blink(0.1)
                    

                if 12 < distance_from_block <= 26:
                    led_blink(0.3)

                if 27 < distance_from_block <= 41:
                    led_blink(0.5)
                    

                if distance_from_block > 40 and distance_from_block < last_distance_from_block:
                    led_blink(1)

                if distance_from_block > 40 and distance_from_block > last_distance_from_block:
                    led_off()

                    
            last_distance_from_block = distance_from_block
            #print(last_distance_from_block)
    mc.postToChat("Thu fannst blokkina!")
    led_off()
    










                    
