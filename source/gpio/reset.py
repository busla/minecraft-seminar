from mcpi.minecraft import Minecraft

mc = Minecraft.create()

mc.player.setPos(-150,17, 100)
print(mc.getPlayerEntityIds())
