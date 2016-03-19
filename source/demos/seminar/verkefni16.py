from mcpi.minecraft import Minecraft
from datetime import datetime
import time

mc = Minecraft.create()

nafn = input('Skrifaðu nafnið þitt: ')
svar = input('Hvaða kyn ertu? (kk/kvk): ')

if svar == 'kk':
    mc.postToChat('hann ' + nafn + ' er kominn inn!')

else:
    mc.postToChat('hun ' + nafn + ' er komin inn!')

while True:
    skilabod = input('Skilaboð: ')

    if skilabod == '':
        print('Þú skrifaðir engan texta, prófaðu aftur!')
    else:
        mc.postToChat(nafn + ": " + skilabod)
