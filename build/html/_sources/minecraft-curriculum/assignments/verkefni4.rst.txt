.. _verkefni4:

Verkefni 4
==========

Prófum að nota aðgerðina *setBlock()* til að smíða kubba.

.. code-block:: python
    
    from mcpi.minecraft import Minecraft

    mc = Minecraft.create()

    hnit = mc.player.getTilePos()
    print(hnit)

    x = hnit.x + 3
    y = hnit.y
    z = hnit.z + 3

    print(x, y, z)

    mc.setBlock(x,y,z, 41)
