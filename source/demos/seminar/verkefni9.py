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

mc.setBlocks(x, y, z, x + lengd_hus, y + haed_hus, z + breidd_hus, 1)

lengd_loft = 8
breidd_loft = 8
haed_loft= 8

x_loft = x + 1
y_loft = y + 1
z_loft = z + 1

# Smíða hús
mc.setBlocks(x_loft, y_loft, z_loft, x_loft + lengd_loft, y_loft + haed_loft, z_loft + breidd_loft, 0)

thak_byrjar = y + haed_hus

lengd = 10
breidd = 10



# Búa til þak sem hefur halla öðru megin
mc.setBlocks(x, # x byrjar
             thak_byrjar, # y byrjar
             z, # z byrjar
             x + lengd, # x endar
             thak_byrjar, # y endar
             z + breidd, # z endar
             5) # Tegund á blokk

mc.setBlocks(x, # x byrjar
             thak_byrjar + 1, # y byrjar
             z, # z byrjar
             x + lengd, # x endar
             thak_byrjar + 1, # y endar
             z + breidd - 1, # z endar
             5) # Tegund á blokk

mc.setBlocks(x, # x byrjar
             thak_byrjar + 2, # y byrjar
             z, # z byrjar
             x + lengd, # x endar
             thak_byrjar + 2, # y endar
             z + breidd - 2, # z endar
             5) # Tegund á blokk

mc.setBlocks(x, # x byrjar
             thak_byrjar + 3, # y byrjar
             z, # z byrjar
             x + lengd, # x endar
             thak_byrjar + 3, # y endar
             z + breidd - 3, # z endar
             5) # Tegund á blokk

mc.setBlocks(x, # x byrjar
             thak_byrjar + 4, # y byrjar
             z, # z byrjar
             x + lengd, # x endar
             thak_byrjar + 4, # y endar
             z + breidd - 4, # z endar
             5) # Tegund á blokk

mc.setBlocks(x, # x byrjar
             thak_byrjar + 5, # y byrjar
             z, # z byrjar
             x + lengd, # x endar
             thak_byrjar + 5, # y endar
             z + breidd - 5, # z endar
             5) # Tegund á blokk
