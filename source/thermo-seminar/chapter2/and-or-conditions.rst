.. _and-or:

Ef að og eða
============

Reglulega notum við fleiri skilyrðingar með *if* og *else*. Í síðasta kafla vildum við athuga hvort auðkennið á blokkinni væri *0*. Hvað ef við viljum athuga hvort blokkinn sé annaðhvort loft eða steinn? Steinn hefur auðkennið *1*, (sjá :ref:`block-constants`).

Búið til nýja skrá sem heiti *verkefni5.py* og setjið inn eftirfarandi kóða.

*Dæmi*

.. code-block:: python

    from mcpi.minecraft import Minecraft

    mc = Minecraft.create()
    nyr_stadur = mc.getBlock(80, 4, 40)

    if nyr_stadur == 0:
        print('Þessi blokk er úr lofti')
    
    elif nyr_stadur == 1:
        print('Þessi blokk er úr steini')
    
    else:
        print('Þessi blokk er hvorki úr lofti né steini')

Það má umorða kóðann svona: Ef kubburinn  á *nýja staðnum* er loft skaltu prenta fyrsta textann, eða ef *nýji staðurinn* eru úr steini skaltu prenta annan textann, annars skaltu prenta þriðja textann. Skipunin *elif* er stytting á *else if*.

Við getum líka farið aðra leið að þessu með því að nota *or*.

*Dæmi*

.. code-block:: python

    from mcpi.minecraft import Minecraft

    mc = Minecraft.create()
    nyr_stadur = mc.getBlock(80, 4, 40)

    if nyr_stadur == 0 or nyr_stadur == 1:
        print('Þessi blokk er úr lofti eða steini')
    
    else:
        print('Þessi blokk er hvorki úr lofti né steini')


Ef blokkin er úr lofti *eða* steini skaltu láta mig vita. Við getum líka athugað hvort blokkin sé úr bæði lofti og steini. Það er auðvitað tilgangslaust skilyrði því að hver blokk getur aðeins verið af einni tegund. En við skulum prófa.

*Dæmi*

.. code-block:: python

    from mcpi.minecraft import Minecraft

    mc = Minecraft.create()
    nyr_stadur = mc.getBlock(80, 4, 40)

    if nyr_stadur == 0 and nyr_stadur == 1:
        print('Þessi blokk er úr lofti og steini')
    
    else:
        print('Þessi blokk er hvorki úr lofti né steini')


Við getum líka blandað öllum þessum skilyrðum saman til að þrengja að þau enn meir. Við gætum t.d. athugað nýja staðsetningin sé úr lofti og hnitið fyrir neðan hann sé úr mold *(id=3)* eða steini.

*Dæmi*

.. code-block:: python

    from mcpi.minecraft import Minecraft

    mc = Minecraft.create()
    nyr_stadur = mc.getBlock(80, 4, 40)
    undir_nyjum_stad = mc.getBlock(5, 7, 9)

    if nyr_stadur == 0 and undir_nyjum_stad == 1 or undir_nyjum_stad == 3:
        print('Þessi blokk er úr lofti og undir henni er blokk úr steini eða mold')
    
    else:
        print('Þessi blokk er ekki úr lofti og blokkin undir henni er hvorki úr mold né steini')


.. _assignment-5:

Verkefni 5
----------
* Finndu út úr því hvort Steve detti um leið og hann er sendur á nýja staðinn.


