from mcpi.minecraft import Minecraft, Vec3
from mcpi import block

mc = Minecraft.create()


def render_tiles(start, end, tile):

    # setBlocks() Byggir marga kubba í einu.
    mc.setBlocks(start.x, start.y, start.z, end.x, end.y, end.z, tile)

start = -127.7
end = 127.7

# Vec3() býr hlut með hnitum. Breyttu y til að hreinsa ákveðna lofthǽð.
block_start = Vec3(start, 0, start)
block_end = Vec3(end, 128, end)

# Sjá Minecraft API í kennsluefninu fyrir allar tegundir (eða block.py í /usr/lib/python3/dist-packages/mcpi)
render_tiles(block_start, block_end, block.AIR)

