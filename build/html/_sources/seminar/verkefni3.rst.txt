.. _verkefni3:

Verkefni 3
==========

Það er hægt að nota reikning til að bæta við breyturnar.

.. code-block:: python
    
    from mcpi.minecraft import Minecraft

    mc = Minecraft.create()

    hnit = mc.player.getTilePos()
    print(hnit)

    x = hnit.x + 10
    y = hnit.y + 10
    z = hnit.z + 10

    print(x, y, z)

    mc.player.setTilePos(x,y,z)
