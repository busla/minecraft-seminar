.. _verkefni13:

Verkefni 13
===========

Kóðinn sem býr til húsið gæti orðið endalaus ef við ætlum alltaf að bæta við nýrri línu þegar við viljum smíða fleiri kubba.

Það er líka erfitt að lesa hann og ef við ætlum að breyta einhverju þá þurfum við að breyta mörgum línum.

Við getum stytt kóðann okkar mjög mikið með því að búa til lykkju sem endurtekur sig eins oft og við viljum.

Fyrst búum við til aðgerð sem við skulum kalla *smida()*. Í hrærivélina setjum við x, y og z hnit en einnig lengd, breidd og hæð. Lykkjan sér um að endurtaka *setBlock()* aðgerðina nokkrum sinnum svo við þurfum ekki að endurtaka okkur.


.. image:: /images/cube-roof-pyramid.jpg


.. code-block:: python
    
    from mcpi.minecraft import Minecraft

    mc = Minecraft.create()

    hnit = mc.player.getTilePos()


    x = hnit.x + 3
    y = hnit.y
    z = hnit.z + 3

    print(x, y, z)


    lengd = 20
    breidd = 40
    haed = 5


    def smida(x, y, z, lengd, breidd, haed):
        lengd_loft = lengd - 2
        breidd_loft = breidd - 2
        haed_loft= haed - 2

        x_loft = x + 1
        y_loft = y + 1
        z_loft = z + 1
        
        # Smíða hús
        mc.setBlocks(x, y, z, x + lengd, y + haed, z + breidd, 1)

        # Gera húsið holt að innan
        mc.setBlocks(x_loft,
                     y_loft,
                     z_loft,
                     x_loft + lengd_loft,
                     y_loft + haed_loft,
                     z_loft + breidd_loft,
                     0)
        
        # Búa til þak sem er eins og píramídi
        thak_byrjar = y + haed

        for i in range(0, 6):
            mc.setBlocks(x + i , # x byrjar
                         thak_byrjar + i, # y byrjar
                         z + i, # z byrjar
                         x + lengd - i, # x endar
                         thak_byrjar + i, # y endar
                         z + breidd - i, # z endar
                         5) # Tegund á blokk

    smida(x, y, z, lengd, breidd, haed)
