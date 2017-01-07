Byggja blokkir
==============

Í kaflanum :ref:`if-else` lærðum við um aðgerðina :meth:`~minecraft.Minecraft.getBlock` til að sækja upplýsingar um blokkir. Núna ætlum við að smíða nýja blokkir með aðgerðinni :meth:`~minecraft.Minecraft.setBlock`. Aðgerðin hefur fjórar færibreytur, *x, y, z, block.id*. Þau gildi sem við sendum með aðgerðinni verða notuð til að smíða blokkina. Við þurfum að senda *x, y, z* hnit og tegund blokkar.

Búið til nýja skrá, sláið inn eftirfarandi kóða og nefnið hana *verkefni7.py*. 

*Dæmi*

.. code-block:: python

    from mcpi.minecraft import Minecraft

    mc = Minecraft.create()
    blokk = mc.setBlock(5, 8, 9, 1)

Engin blokk? Það er skiljanlegt því þú ert ekkert endilega á sama stað og hnitið sem þú sendir í færibreyturnar.

.. _assignment-7:

Verkefni 7
__________

* Settu blokk einhverstaðar nálægt Steve (nota aðgerðir úr :ref:`assignment-3`)

