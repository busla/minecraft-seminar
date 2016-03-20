.. _verkefni7:

Verkefni 7
==========

Í síðasta verkefni bjuggum við til hús. Til að húsið holt að innan þurfum við að fylla upp í það með lofti. Loft kubbur hefur auðkennið 1.


.. image:: /images/cube-coordinates.jpg

Ímyndum okkur nú að þetta sé húsið sem við smíðuðum. Hvaða hnit þurfum við að fylla upp í með lofti?


.. code-block:: python
    
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

    # Smíða kassa
    mc.setBlocks(x, y, z, x + lengd, y + haed, z + breidd, 5)

    lengd_loft = 8
    breidd_loft = 8
    haed_loft= 8

    x_loft = x + 1
    y_loft = y + 1
    z_loft = z + 1

    # Setja loft kubba inn í kassann svo hann verði holur að innan
    mc.setBlocks(x_loft, y_loft, z_loft, x_loft + lengd_loft, y_loft + haed_loft, z_loft + breidd_loft, 0)

