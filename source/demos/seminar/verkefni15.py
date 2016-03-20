from mcpi.minecraft import Minecraft
from datetime import datetime
import time

mc = Minecraft.create()

nafn = input("Skrifaðu nafnið þitt: ")
mc.postToChat(nafn + " er kominn inn!")

while True:
    skilabod = input("Skilaboð: ")
    mc.postToChat(nafn + ": " + skilabod)
