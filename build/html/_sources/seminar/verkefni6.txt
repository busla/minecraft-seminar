.. _verkefni6:

Verkefni 6
==========

Með því að nota aðgerðina *setBlocks()* getum við byggt marga kubba í einu. Við veljum frá hvaða hniti við viljum byrja og hvar við viljum enda.

Prófum næst að smíða hús.



.. image:: /images/cube-coordinates.jpg

Ímyndum okkur að þetta sé Minecraft heimurinn. Til að velja svæðið sem þú vilt byggja kubba velurðu frá hvaða hniti þú vilt byggja og hvar þú vilt hætta.


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

    mc.setBlocks(x, y, z, x + lengd, y + haed, z + breidd, 5)
