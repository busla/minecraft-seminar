Listar
======

Í kaflanum um :doc:`../day2/and-or-conditions` notuðum við samanburðaraðgerðir til að athuga hvort gildi voru sönn eða ósönn. Þú tókst kannski eftir því að við vorum að endurtaka breytuna *nyr_stadur* margoft þegar við bárum hana saman við önnur gildi. Innan Python samfélagsins er oft talað um *DRY* regluna, *Don´t repeat yourself*, eða *Ekki endurtaka þig*.

Með því að nota lista (oft kallað *fylki*) getum við fækkað þessum endurtekningum á breytunni *nyr_stadur*. 

En hvað eru listar?

Listi er ein breyta sem geymir mörg gildi í einu safni. Rétt eins og þú getur geymt allskonar vörur í innkaupakerru þegar þú ferð út í búð. Hvert gildi er aðskilið með *,* (kommu). Það er hægt að geyma hvaða gildi sem er í safninu, þau þurfa ekki að vera af sömu tegund. Til að búa til safn þá notarðu hornklofa til að geyma safnið, *[]*.

*Dæmi*

>>> ['Jón', 2, 'þetta er einhver texti', '78.9']
['Jón', 2, 'þetta er einhver texti', '78.9']

Ef við viljum geyma safnið í breytu þá skilgreinum við hana.

>>> safnid_mitt = [1, 2, 3, 4, 5]
>>> safnid_mitt
[1, 2, 3, 4, 5]

Við getum líka athugað hvort safnið innihaldi eitthvað gildi með því að nota samanburðaraðgerðina *in*.

>>> 'jón' in ['jón', 'ásgerður', 'flóki']
True

>>> 'björk' in ['jón', 'ásgerður', 'flóki']
False

Eða athugað hvort breytan okkar (sem er listi) innihaldi eitthvað gildi.

>>> safnid_mitt = [1, 2, 3, 4, 5]
>>> 3 in safnid_mitt
True

Kíkjum núna aftur á kóðann sem við skrifuðum í :doc:`../day2/and-or-conditions` og athugum hvort við getum breytt honum með því að nota lista.

*Dæmi*

.. code-block:: python

    from mcpi.minecraft import Minecraft

    mc = Minecraft.create()
    nyr_stadur = mc.getBlock(5, 8, 9)

    if nyr_stadur.id in 0 or nyr_stadur.id in 1:
        print('Þessi blokk er úr lofti eða steini')
    
    else:
        print('Þessi blokk er hvorki úr lofti né steini')


.. code-block:: bash

    Traceback (most recent call last):
      File "<stdin>", line 6, in <module>
    TypeError: argument of type 'int' is not iterable  

Þetta virkar ekki og við fáum villu. Þarna kemur fram að í 6. línu sé *int* sé ekki áréttanleg, þ.e. það er ekki hægt að fara í gegnum hana skref fyrir skref.

.. code-block:: python

    if nyr_stadur.id in 0 or nyr_stadur.id in 1:

Það er skiljanlegt því *0* er ekki safn og því ekki hægt að fara í gegnum töluna skref fyrir skref, því þetta er bara ein tala.

Safn þarf ekki að hafa mörg gildi, eitt er nóg en við verðum að nota *[]* til að breyta tegundinni yfir í safn. Prófum aftur.

*Dæmi*

.. code-block:: python

    from mcpi.minecraft import Minecraft

    mc = Minecraft.create()
    nyr_stadur = mc.getBlock(5, 8, 9)
    undir_nyjum_stad = mc.getBlock(5, 7, 9)

    if nyr_stadur.id in 0 or nyr_stadur.id in 1:
        print('Þessi blokk er úr lofti eða steini')

    else:
        print('Þessi blokk er hvorki úr lofti né steini')

Þetta er betra.

Prófum núna að stytta kóðan okkar með því að nota *nyr_stadur.id* bara einu sinni.

*Dæmi*

.. code-block:: python

    from mcpi.minecraft import Minecraft

    mc = Minecraft.create()
    nyr_stadur = mc.getBlock(5, 8, 9)
    undir_nyjum_stad = mc.getBlock(5, 7, 9)

    if nyr_stadur.id in [0, 1]:
        print('Þessi blokk er úr lofti eða steini')

    else:
        print('Þessi blokk er hvorki úr lofti né steini')

Hér athugum við hvort safnið [0, 1] sé með gildið úr *nyr_stadur.id* og það er satt.

Öll gildin í safninu hafa sætisnúmer. Rétt eins og í flugvél þá fær hver farþegi sitt sætisnúmer. Sætisnúmerin í listum byrja á *0* en ekki *1*. Prófum að búa til flugvél með farþegasætum og setjum nokkra farþega þar inn. Til að athuga í hvaða sætisnúmeri farþegarnir eru notum við aðgerðina *index*, á íslensku *atriðaskrá*.

>>> flugvel = ['Jónatan', 'Sandra', 'Eyrún', 'Finnur', 'Kristín']
>>> flugvel.index('Jónatan')
0
>>> flugvel.index('Sandra')
1
>>> flugvel.index('Eyrún')
2

Ef við notum sætisnúmerið þá getum við athugað hvaða farþegi situr þar.

>>> flugvel[3]
'Finnur'

Hér setjum við hornklofann strax á eftir safninu til að gefa til kynna hvaða sætisnúmer við viljum fá gildið úr.

Annað sem við getum gert er að bæta við gildum í safnið. Við getum notað aðgerðirnar *append()* og *insert()*

Aðgerðin *append()* setur nýja gildið aftast í safnið.

>>> flugvel.append('Stefanía')
>>> flugvel
['Jónatan', 'Sandra', 'Eyrún', 'Finnur', 'Kristín', 'Stefanía']
 
 Aðgerðin *insert()* setur gildi í það sæti sem við viljum og ýtir restinni til hliðar.

>>> flugvel.insert(4, 'Eiríkur')
>>> flugvel
['Jónatan', 'Sandra', 'Eyrún', 'Finnur', 'Eiríkur', 'Kristín', 'Stefanía']
 

.. _assignment-8:

Verkefni 8
__________

* Búðu til safn með nokkrum blokkum (notaðu auðkenni þeirra)
* Bjóddu notandanum upp á að slá inn auðkenni blokkar (sjá :doc:`../day2/input`)
* Settu nýja blokk (sjá :meth:`~minecraft.Minecraft.setBlock`) af tegundinni sem var slegin inn fyrir framan, aftan og hliðina á Steve (nota *x ás* og *z ás*)