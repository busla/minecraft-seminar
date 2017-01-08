.. _verkefni2:

Verkefni 2
==========

Útskýra hnit.

.. code-block:: python
    
    from mcpi.minecraft import Minecraft

    mc = Minecraft.create()

    hnit = mc.player.getTilePos()
    print(hnit)

    x = hnit.x
    y = hnit.y
    z = hnit.z

    print(x, y, z)
