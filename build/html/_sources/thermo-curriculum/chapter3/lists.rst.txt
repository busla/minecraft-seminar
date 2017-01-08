.. _thermo-lists:

Listar
==========

Listi er ein breyta sem geymir mörg gildi. Rétt eins og þú getur sett allskyns vörur á innkaupalistann áður en þú ferð út í búð. Hvert gildi er aðskilið með *,* (kommu). Það er hægt að geyma hvaða gildi sem er á listanum, þau þurfa ekki að vera af sömu tegund. Til að búa til lista þá notarðu hornklofa til að geyma listann, *[]*.

Búðu til skrána *verkefni10.py*.

*Dæmi*

.. code-block:: python

    listi = ['Jón', 2, False, 78.9]
    print(listi)

Í listanum hér fyrir ofan erum við að geyma streng, integer, boolean og float

Við getum líka athugað hvort listinn innihaldi eitthvað gildi með því að nota samanburðaraðgerðina *in*.

.. code-block:: python

    listi = ['Jón', 2, False, 78.9]
    if 'Jón' in listi:
        print('Jón er í listanum')
    else:
        print('Jón er ekki í listanum')


Við getum líka prentað út samanburðaraðgerðina sjálfa:

.. code-block:: python

    listi = ['Jón', 2, False, 78.9]
    print('Jón' in listi)


Við getum prentað út gildið í ákveðnu sæti.

.. code-block:: python

    listi = ['Jón', 'Sámur', 'Friðrik', 'Grundafjörður', 'Sigmundur Davíð', 'Drullumall']    
    print(listi[2])


Við getum notað *slice()* aðgerðina til að prenta aðeins hluta úr listanum, þ.e. sætisnúmer *[frá:til]*

.. code-block:: python

    listi = ['Jón', 'Sámur', 'Friðrik', 'Grundafjörður', 'Sigmundur Davíð', 'Drullumall']    
    print(listi[0:2]) # print(listi[:2]) skilar sömu niðurstöðu


Eða talið frá síðasta sætinu

.. code-block:: python

    listi = ['Jón', 'Sámur', 'Friðrik', 'Grundafjörður', 'Sigmundur Davíð', 'Drullumall']    
    print(listi[-1]) # prenta gildið í síðasta sætinu
    print(listi[-2]) # prenta gildið í næstsíðasta sætinu



Listar hafa fjölda aðgerða. 

.. _list-append:

append()
__________

.. code-block:: python
    
    listi = [] # breyta með tómum lista
    listi.append('Nýtt gildi') # bætir við gildi aftast í listann
    listi.append('Jón')
    listi.append(2)
    listi.append(True)
    print(listi)

.. _list-pop:

pop()
__________

.. code-block:: python

    listi = ['Jón', 2, False, 78.9]
    listi.pop() # fjarlægja síðasta gildið úr listanum
    print(listi)


.. code-block:: python

    listi = ['Jón', 2, False, 78.9]
    listi.pop(0) # fjarlægja gildi í sætinu 0
    print(listi)


.. _list-insert:

insert()
__________

.. code-block:: python

    listi = ['Jón', 2, False, 78.9]
    listi.insert(1, 'Nýtt gildi') # bæta við gildi í sæti 1 og ýta restinni áfram um eitt sæti.
    print(listi)


.. _list-remove:

remove()
__________

.. code-block:: python

    listi = ['Jón', 2, False, 78.9]
    listi.remove('Jón') # fjarlægja gildi úr listanum
    print(listi)


.. _list-extend:

extend()
__________

.. code-block:: python

    listi1 = ['Jón', 2, False, 78.9]
    listi2 = ['Sámur', 15, True, 58.459]
    listi1.extend(listi2) # sameina listi2 við listi1
    print(listi1)



.. _list-index:

index()
__________

.. code-block:: python

    listi = ['Jón', 2, False, 78.9, 'Sámur', 15, True, 58.459]
    print(listi.index(78.9)) # í hvaða sæti er gildið
    

.. _list-sort:

sort()
__________

.. code-block:: python

    listi = ['Jón', 'Sámur', 'Friðrik', 'Grundafjörður', 'Sigmundur Davíð', 'Drullumall']
    listi.sort()
    print(listi)
  

.. _list-reverse:

reverse()
__________

.. code-block:: python

    listi = ['Jón', 'Sámur', 'Friðrik', 'Grundafjörður', 'Sigmundur Davíð', 'Drullumall']
    listi.reverse() # endurraðar listanum í öfugri röð
    print(listi)


Við getum einnig sett lista inn í lista.

.. code-block:: python

    listi1 = ['Jón', 'Sámur', 'Friðrik']
    listi2 = ['Grundafjörður', 'Sigmundur Davíð', 'Drullumall']
    listi.append(listi2)
    print(listi1)



Búum til lista með *list()* aðgerðinni.

.. code-block:: python

    listi = list("Þetta er í annað sinn á innan við mánuði sem rúta með ferðamönnum fer út af veginum á Mosfellsheiði. 20. desember valt rúta með átján farþegum. Þar slasaðist heldur enginn alvarlega.")
    print(list)


.. _thermo-assignment-10:

Verkefni 10
____________

* Notaðu *for* lykkju til að bæta við 10 slembitölum í lista
* Prentaðu út hæstu töluna í listanum. Notaðu netið til að finna lausn.
