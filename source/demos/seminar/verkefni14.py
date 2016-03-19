from mcpi.minecraft import Minecraft
from datetime import datetime
import time

mc = Minecraft.create()

while True:
    print(datetime.now())
    time.sleep(1)
