Orðasöfn
=================

Orðasöfn *(dictionaries)* eru svipaðar listum að því leiti að við getum geymt safn af gildum. Munurinn er þó sá að í stað þess að nota sætisnúmer líkt og við gerðum með flugvélina í kaflanum :doc:`lists` þá getum við nefnt sætin *vinstri* og *hægri*. Sætin *0* og *1* í listanum segir okkur ekki mikið um hvoru meginn í flugvélinni fólkið sat.

Í orðasöfnum notum við lýsandi orð til að flokka gildin okkar. Í stað þess að nota hornklofa *[]* (brackets) notum við krullur *{}* (braces).

Gildið okkar fær því sitt eigið heiti. Heitið og gildið sjálft er síðan aðskilið með tvípunkti. Oft er talað um *lykil* og *gildi* (á ensku *key, value* )

*Dæmi*

>>> nemandi = {'nafn': 'Jón', 'netfang': 'koder@koder.is', 'aldur': 34}
>>> nemandi
{'aldur': 34, 'netfang': 'koder@koder.is', 'nafn': 'Jón'}

Í þessu dæmi þá hefur t.d. lykillinn *'nafn'* gildið *'Jón'*. Takið eftir að orðasafnið er ekki í sömu röð og við slógum það inn því við erum ekki að nota sæti líkt og í listum. Við hrúgum bara öllu inn og getum svo raðað því seinna ef við viljum. Í dæminu sjáiði við notum streng í gildunum fyrir nafn og netfang en heila tölu fyrir aldur. Líkt og í listum getum við notað hvaða tegund sem er.

Búið til skrá og nefnið hana *verkefni9.py*. Sláið síðan inn eftirfarandi kóða. Í stað þess að hafa hann allan í einni línu þá gerum við hann snyrtilegan og notum fjögur bil eins og við lærðum í :doc:`../day2/if-else-conditions`.

.. code-block:: python

    nemandi = {
        'nafn': 'Jón',
        'netfang': 'koder@koder.is',
        'aldur': 34,
        'systkini': ['Gunnar', 'Inga', 'Ástrós']
    }

    print(nemandi)

Keyrið síðan kóðann.

.. code-block:: bash
    
    $ python3 verkefni9.py

.. note::

    Af hvaða tegund er lykillinn *systkini* ?

Til að sækja gildi úr orðasafni þá notum við lykilinn. Við sækjum það eins og við sækjum gildi úr lista (sjá :doc:`lists`) en notum lykilinn í staðinn fyrir sætið.

>>> nemandi['nafn']
'Jón'


Við getum líka notað aðgerðina *get()* til að sækja gildið.

>>> nemandi.get('nafn')
'Jón'

Athugum hvort orðasafnið sé með ákveðinn lykil.

>>> nemandi.has_key('nafn')
True

>>> nemandi.has_key('skónúmer')
False


Í þessu orðasafni erum við að geyma einn nemanda. Hvað ef við viljum geyma marga nemendur? Oft notum við lista og orðasöfn saman. Í þessu tilfelli getum við búið til lista af nemendum. Þá fær hvert sæti í listanum orðasafn af hverjum nemanda.

.. _assignment-9:
    
Verkefni 9
__________

* Búðu til lista sem geymir þrjá nemendur. Hver nemandi skal vera orðasafn.
