Byggja blokkir
==============

Í kaflanum :doc:`../day2/if-else-conditions` lærðum við um aðgerðina :meth:`~minecraft.Minecraft.getBlock` til að sækja upplýsingar um blokkir. Núna ætlum við að smíða nýja blokkir með aðgerðinni :meth:`~minecraft.Minecraft.setBlock`. Aðgerðin hefur fjórar færibreytur, *x, y, z, block.id*. Þau gildi sem við sendum með aðgerðinni verða notuð til að smíða blokkina. Við þurfum að senda *x, y, z* hnit og tegund blokkar.

*Dæmi*

.. code-block:: python

    from mcpi.minecraft import Minecraft

    mc = Minecraft.create()
    nyr_stadur = mc.getBlock(5, 8, 9)

    if nyr_stadur.id == 1:
        print('Þessi blokk er úr lofti')
    
    else:
        print('Þessi blokk er úr hörðu efni og þú munt festast')


