.. _verkefni10:

Verkefni 10
===========

Í síðasta verkefni settum við skáhallandi þak á húsið með því að sleppa því að byggja kubb í hvert skipti sem við hækkuðum *y ás*.

Nú ætlum við að hafa þakið hallandi báðu meginn. Þá þurfum við að sleppa því að byggja kubb báðu meginn á *z ásnum* þegar við hækkum okkur.

.. image:: /images/cube-roof-traditional.jpg


.. code-block:: python
    
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
    haed = 5


    # Búa til þak sem hefur halla báðu meginn
    mc.setBlocks(x, # x byrjar
                 thak_byrjar, # y byrjar
                 z, # z byrjar
                 x + lengd, # x endar
                 thak_byrjar, # y endar
                 z + breidd, # z endar
                 5) # Tegund á blokk

    mc.setBlocks(x, # x byrjar
                 thak_byrjar + 1, # y byrjar
                 z + 1, # z byrjar
                 x + lengd, # x endar
                 thak_byrjar + 1, # y endar
                 z + breidd - 1, # z endar
                 5) # Tegund á blokk

    mc.setBlocks(x, # x byrjar
                 thak_byrjar + 2, # y byrjar
                 z + 2, # z byrjar
                 x + lengd, # x endar
                 thak_byrjar + 2, # y endar
                 z + breidd - 2, # z endar
                 5) # Tegund á blokk

    mc.setBlocks(x, # x byrjar
                 thak_byrjar + 3, # y byrjar
                 z + 3, # z byrjar
                 x + lengd, # x endar
                 thak_byrjar + 3, # y endar
                 z + breidd - 3, # z endar
                 5) # Tegund á blokk

    mc.setBlocks(x, # x byrjar
                 thak_byrjar + 4, # y byrjar
                 z + 4, # z byrjar
                 x + lengd, # x endar
                 thak_byrjar + 4, # y endar
                 z + breidd - 4, # z endar
                 5) # Tegund á blokk

    mc.setBlocks(x, # x byrjar
                 thak_byrjar + 5, # y byrjar
                 z + 5, # z byrjar
                 x + lengd, # x endar
                 thak_byrjar + 5, # y endar
                 z + breidd - 5, # z endar
                 5) # Tegund á blokk
