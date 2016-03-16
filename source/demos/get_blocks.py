from mcpi.minecraft import Minecraft
from mcpi.vec3 import Vec3

mc = Minecraft.create()
start = -127.7
end = 127.7

# Vec3() býr hlut með hnitum. Breyttu y til að hreinsa ákveðna lofthǽð.
block_start = Vec3(start, 0, start)
block_end = Vec3(end, 128, end)

#print(mc.getBlocks(block_start.x, block_start.y, block_start.z, block_end.x, block_end.y, block_end.z))
print(mc.getBlocks(1.1,1.1,1.1,3.1,3.1,3.1))
