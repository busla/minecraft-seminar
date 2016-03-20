.. _verkefni5:

Verkefni 5
==========

Prófum að setja margar blokkir.

.. code-block:: python
    
    from mcpi.minecraft import Minecraft

    mc = Minecraft.create()

    hnit = mc.player.getTilePos()
    print(hnit)

    x = hnit.x + 3
    y = hnit.y
    z = hnit.z + 3

    print(x, y, z)

    mc.setBlock(x, y, z, 41)
    mc.setBlock(x+1, y, z, 41)
    mc.setBlock(x+2, y, z, 41)
    mc.setBlock(x+3, y, z, 41)

