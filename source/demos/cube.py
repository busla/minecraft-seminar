from mcpi.minecraft import Minecraft
import random

mc = Minecraft.create()

steve = mc.player.getPos()

x = steve.x + 5
y = steve.y
z = steve.z + 5

x_cube = list(range(0, 10))
y_cube = list(range(0, 10))
z_cube = list(range(0, 10))

cube_min = min(x_cube)
cube_max = max(x_cube)

tiles = [5, 14, 16, 20, 22, 35, 4, 46, 45, 49, 57, 73, 80, 103, 246, 247]

for i in x_cube:     
    for r in y_cube:
        for n in z_cube:
            if (n == cube_min or n == cube_max) or (i == cube_min or i == cube_max) or (r == cube_min or r == cube_max):            
                mc.setBlock(x+i, y+r, z+n, random.choice(tiles))
            else:
                mc.setBlock(x+i, y+r, z+n, 0)            
