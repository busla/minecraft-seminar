.. _verkefni1:

Verkefni 1
==========

Smíða hús og skoða hnitin efst í vinstra horninu. Útskýra verkfærakassa og verkfæri.

.. code-block:: python
    
    from mcpi.minecraft import Minecraft

    mc = Minecraft.create()

    hnit = mc.player.getTilePos()
    print(hnit)
