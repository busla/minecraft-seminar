.. _thermo-dictionaries:

Orðasöfn
=================

Orðasöfn *(dictionaries)* eru svipaðar listum að því leiti að við getum geymt safn af gildum. Munurinn er þó sá að í stað þess að nota sætisnúmer líkt og við gerðum með flugvélina í kaflanum :ref:`thermo-lists` þá getum við nefnt sætin *vinstri* og *hægri*. Sætin *0* og *1* í listanum segir okkur ekki mikið um hvoru meginn í flugvélinni fólkið sat.

Í orðasöfnum notum við lýsandi orð til að flokka gildin okkar. Í stað þess að nota hornklofa *[]* (brackets) notum við krullur *{}* (braces).

Gildið okkar fær því sitt eigið heiti. Heitið og gildið sjálft er síðan aðskilið með tvípunkti. Oft er talað um *lykil* og *gildi* (á ensku *key, value* )

*Dæmi*

>>> nemandi = {'nafn': 'Jón', 'netfang': 'koder@koder.is', 'aldur': 35}
>>> nemandi
{'aldur': 35, 'netfang': 'koder@koder.is', 'nafn': 'Jón'}

Í þessu dæmi þá hefur t.d. lykillinn *'nafn'* gildið *'Jón'*. Takið eftir að orðasafnið er ekki í sömu röð og við slógum það inn því við erum ekki að nota sæti líkt og í listum. Við hrúgum bara öllu inn og getum svo raðað því seinna ef við viljum. Í dæminu sjáiði við notum streng í gildunum fyrir nafn og netfang en heila tölu fyrir aldur. Líkt og í listum getum við notað hvaða tegund sem er.

Búið til skrá og nefnið hana *verkefni11.py*. Sláið síðan inn eftirfarandi kóða. Í stað þess að hafa hann allan í einni línu þá gerum við hann snyrtilegan og notum fjögur bil eins og við lærðum í :ref:`thermo-if-else`.

.. code-block:: python

    nemandi = {
        'nafn': 'Jón',
        'netfang': 'koder@koder.is',
        'aldur': 35,
        'systkini': ['Gunnar', 'Inga', 'Ástrós']
    }

    print(nemandi)


.. note::

    Af hvaða tegund er lykillinn *systkini* ?

Til að sækja gildi úr orðasafni þá notum við lykilinn. Við sækjum það eins og við sækjum gildi úr lista (sjá :ref:`thermo-lists`) en notum lykilinn í staðinn fyrir sætið.

>>> nemandi['nafn']
'Jón'


Við getum líka notað aðgerðina *get()* til að sækja gildið.

>>> nemandi.get('nafn')
'Jón'

Athugum hvort orðasafnið sé með ákveðinn lykil.

>>> 'nafn' in nemandi
True

>>> 'skónúmer' in nemandi
False


Breytan *nemandi* geymir eitt orðasafn (dictionary). Hvað ef við viljum geyma mörg orðasöfn í einni breytu, t.d. marga nemendur?

Við gætum notað lista sem geymir eitt orðasafn í hverju sæti.

.. code-block:: python
    
    listi = []
    
    hiti1 = {
        'dagsetning': '2016-06-19 15:25:36',
        'hiti': 23.574,
        'skynjari': 'herbergi'        
    }

    hiti2 = {
        'dagsetning': '2016-06-19 16:35:10',
        'hiti': 21.325,
        'skynjari': 'herbergi'        
    }

    listi.append(hiti1)
    listi.append(hiti2)
    print(listi)


.. _thermo-assignment-11:
    
Verkefni 11
__________

* Skilgreindu breytu með lista af nöfnum á rými þar sem skynjarar eru staðsettir (stofa, baðherbergi, eldhús)
* Notaðu *for* lykkju til að búa til 10 orðasöfn og bættu hverju safni við í listann.
* Notaðu slembitölu fyrir hitastig.
* Módúlan *random* kemur með aðgerð sem þú getur notað til að velja skynjara með hlutkesti. Finndu þessa aðgerð og notaðu hana.
* Lestu um *datetime* módúluna og notaðu hana til að setja tímann núna, *now()*, sem dagsetningu og tíma.
