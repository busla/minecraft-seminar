from mcpi.minecraft import Minecraft
from datetime import datetime
import time

mc = Minecraft.create()

nafn = input("Skrifaðu nafnið þitt: ")
mc.postToChat(nafn + " er komin inn!")

while True:
    skilabod = input("Skilaboð: ")
    mc.postToChat(nafn + ": " + skilabod)
