from mcpi.minecraft import Minecraft

mc = Minecraft.create()

hnit = mc.player.getTilePos()


x = hnit.x + 3
y = hnit.y
z = hnit.z + 3

print(x, y, z)


lengd = 10
breidd = 10
haed = 10

mc.setBlocks(x, y, z, x + lengd, y + haed, z + breidd, 5)
