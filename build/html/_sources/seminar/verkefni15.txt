.. _verkefni15:

Verkefni 15
===========

Nú skulum við prófa að nota lykkju til að gera eitthvað skemmtilegt í Minecraft.

Við ætlum að nota aðgerðina *input()* sem stoppar forritið og bíður eftir því að við sláum inn texta í *Terminal*.

Þegar við höfum slegið inn texta og ýtt á ENTER þá heldur forritið áfram í næstu línu.

Hvað er að gerast í þessum kóða?

.. code-block:: python
    
    from mcpi.minecraft import Minecraft
    from datetime import datetime
    import time

    mc = Minecraft.create()

    nafn = input("Skrifaðu nafnið þitt: ")
    mc.postToChat(nafn + " er komin inn!")

    while True:
        skilabod = input("Skilaboð: ")
        mc.postToChat(nafn + ": " + skilabod)

Hér smá vandamál. Orðið *komin* er með einu *n* svo að textinn er bara réttur ef þú ert stelpa. Hvernig getum við skrifað *kominn* ef þú ert strákur?
