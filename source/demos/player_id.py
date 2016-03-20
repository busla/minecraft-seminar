from mcpi.minecraft import Minecraft

mc = Minecraft.create()
mc.postToChat('Thu ert numer: %d' % mc.getPlayerEntityIds()[0])
