Hvað ef?
========

Við virðumst ekki geta stjórnað því hvort Steve lendi inni í fjalli eða ekki. Við sendum hann bara á það hnit sem við viljum og hann er sendur þangað. Væri ekki gott ef við gætum athugað hvort hann festist eða ekki?

Steve festist ef það er blokk úr efni á sama hniti og við sendum hann á. Skoðum lista yfir blokkirnar

Í Minecraft er *loft* einnig blokk. Hún er ekki sýnileg og leyfir okkur að ganga í gegnum hana. En þetta er blokk engu að síður. Allar blokkir í Minecraft hafa auðkenni. Kíktu á lista yfir auðkenni allra blokka í Minecraft (:ref:`block-constants`)


Sem dæmi þá hefur *AIR* auðkennið *1*. Áður en við sendum Steve á nýtt hnit þá getum við athugað hvort það sé *AIR* blokk á hnitinu. Það ætti að koma í veg fyrir að hann festist inn í miðju fjalli.

Til að sækja upplýsingar um blokkir getum við notað aðgerðina :meth:`~minecraft.Minecraft.getBlock`. Þessi aðgerð tekur við hnitum og skilar okkur tilbaka tegundinni á blokkinni.

*Dæmi*

>>> from mcpi.minecraft import Minecraft
>>> mc = Minecraft.create()
>>> mc.getBlock(5, 8, 9)

.. todo::
    Vantar result

Prófiði þar til þið fáið blokk með auðkennið *1*. Við getum líka búið til skilyrði til að fá betri lýsingu á því hvaða blokk þetta er. Opniði núna forritið *IDLE3* svo við þurfum ekki að skrifa þetta allt í *Terminal*.

*Dæmi*

.. code-block:: python

    from mcpi.minecraft import Minecraft

    mc = Minecraft.create()
    blokk = mc.getBlock(5, 8, 9)

    print(blokk)

Vistið þessa skrá sem *verkefni4.py*. Nú getiði keyrt kóðann ykkar með því að skrifa:

.. code-block:: bash
    
    $ python3 athuga_blokk.py

Hér biðjum við *Python* að túlka allt sem finnst í *athuga_blokk.py* skránni. Ef þið viljið endurtaka skipunina þá notiði *upp* örina á lyklaborðinu til að skoða söguna á öllum skipunum sem þið hafið slegið inn.

Kíkjum aftur á kóðan og búum til skilyrði sem athugar hvort blokkin sé *AIR*. Til þess notum við *if* og *else* skilyrðingu, þ.e.a.s. *ef* blokkin er af tegundinni *AIR* þá skaltu prenta texta á skjánum sem segir með það, *annars* skaltu prenta texta á skjánum sem segir mér að hún sé það ekki.

*Dæmi*

.. code-block:: python

    from mcpi.minecraft import Minecraft

    mc = Minecraft.create()
    nyr_stadur = mc.getBlock(5, 8, 9)

    if nyr_stadur.id == 1:
        print('Þessi blokk er úr lofti')
    
    else:
        print('Þessi blokk er úr hörðu efni og þú munt festast')



Skoðum þennan kóða aðeins betur því að er ýmislegt að gerast í honum. Þegar við notum tvö samasem merki *==* þá erum við að nota *samanburðaraðgerð*. Í :doc:`../day1/python-shell` notuðum við eitt *=* merki til að gefa einhverri breytu gildi, sem myndi kallast *gildisaðgerð*. Það er algengt að við ruglumst á þessu þegar við erum að læra um aðgerðir.

Þegar við notum samanburð til að bera saman tvö gildi þá er samanburðurinn annaðhvort sannur eða ósannur. Sem dæmi þá er *1 == 2* ósannur því 1 er ekki það sama og tveir. Hér fyrir ofan erum við að bera saman auðkennið á blokkinni við töluna *0*. Ef samanburðurinn er sannur þá vil ég framkvæma allar aðgerðir sem koma á eftir tvípunktinum og hafa fjögur bil í inndrátt.

Python er mjög strangt þegar það kemur að inndrætti og skilar villu ef það eru færri eða fleiri bil. Þetta er gert til að það sé samræmi í öllum Python kóða sem við munum koma til með að skrifa og svo það sé auðskiljanlegt að lesa kóða frá öðrum.

Hvað gerist ef við færum *print()* skipunina aftur um fjögur bil?

*Dæmi*

.. code-block:: python

    from mcpi.minecraft import Minecraft

    mc = Minecraft.create()
    nyr_stadur = mc.getBlock(5, 8, 9)

    if nyr_stadur.id == 0:
        print('Þessi blokk er úr lofti')
    
    else:
        print('Þessi blokk er úr hörðu efni og þú munt festast')


Við fáum villu því að það er tilgangslaust að vera með samanburð og framkvæma ekkert ef hann er sannur/ósannur. En ef við bætum við skipun á eftir *else* ?

*Dæmi*

.. code-block:: python

    from mcpi.minecraft import Minecraft

    mc = Minecraft.create()
    nyr_stadur = mc.getBlock(5, 8, 9)

    if nyr_stadur.id == 0:
        print('Þessi blokk er úr lofti')
    
    else:
        print('Þessi blokk er úr hörðu efni og þú munt festast')

    print('Þessi texti birtist alltaf í lokin')



.. _assignment-4:

Verkefni 4
----------
* Finndu út úr því hvort það sé loft Steve detti um leið og hann er sendur á nýja staðinn.
* Sendu Steve á nýja staðinn ef blokkin þar er úr lofti. Þú þarft að nota aðgerðir úr :ref:`assignment-3`.