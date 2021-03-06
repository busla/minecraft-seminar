from mcpi.minecraft import Minecraft

mc = Minecraft.create()

hnit = mc.player.getTilePos()


x = hnit.x + 3
y = hnit.y
z = hnit.z + 3

print(x, y, z)


lengd_hus = 10
breidd_hus = 10
haed_hus = 5

# Smíða hús
mc.setBlocks(x, y, z, x + lengd_hus, y + haed_hus, z + breidd_hus, 1)

lengd_loft = 8
breidd_loft = 8
haed_loft= 8

x_loft = x + 1
y_loft = y + 1
z_loft = z + 1

# Setja loft kubba inn í kassann svo hann verði holur að innan
mc.setBlocks(x_loft, y_loft, z_loft, x_loft + lengd_loft, y_loft + haed_loft, z_loft + breidd_loft, 0)

thak_byrjar = y + haed_hus

lengd = 10
breidd = 10


# Búa til þak sem er eins og píramídi
mc.setBlocks(x, # x byrjar
             thak_byrjar, # y byrjar
             z, # z byrjar
             x + lengd, # x endar
             thak_byrjar, # y endar
             z + breidd, # z endar
             5) # Tegund á blokk

mc.setBlocks(x + 1, # x byrjar
             thak_byrjar + 1, # y byrjar
             z + 1, # z byrjar
             x + lengd - 1, # x endar
             thak_byrjar + 1, # y endar
             z + breidd - 1, # z endar
             5) # Tegund á blokk

mc.setBlocks(x + 2, # x byrjar
             thak_byrjar + 2, # y byrjar
             z + 2, # z byrjar
             x + lengd - 2, # x endar
             thak_byrjar + 2, # y endar
             z + breidd - 2, # z endar
             5) # Tegund á blokk

mc.setBlocks(x + 3, # x byrjar
             thak_byrjar + 3, # y byrjar
             z + 3, # z byrjar
             x + lengd - 3, # x endar
             thak_byrjar + 3, # y endar
             z + breidd - 3, # z endar
             5) # Tegund á blokk

mc.setBlocks(x + 4, # x byrjar
             thak_byrjar + 4, # y byrjar
             z + 4, # z byrjar
             x + lengd - 4, # x endar
             thak_byrjar + 4, # y endar
             z + breidd - 4, # z endar
             5) # Tegund á blokk

mc.setBlocks(x + 5, # x byrjar
             thak_byrjar + 5, # y byrjar
             z + 5, # z byrjar
             x + lengd - 5, # x endar
             thak_byrjar + 5, # y endar
             z + breidd - 5, # z endar
             5) # Tegund á blokk

# Á hvaða hnit þarf Steve að fara? Getur verið að hann þurfi að fara á síðasta kubbinn sem þú byggir?
mc.player.setTilePos()