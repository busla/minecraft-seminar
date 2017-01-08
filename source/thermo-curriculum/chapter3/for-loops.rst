.. _thermo-for-loops:

For lykkjur
=================

Í kaflanum um While lykkjur þá sáum við hvernig við gátum skilgreint teljara og farið úr lykkjunni ef teljarinn mætti ákveðnu skilyrði. Í *for* lykkjum þá skilgreinum við breytu sem hluta af lykkjunni sem fær sjálfkrafa nýtt gildi í hverjum hring sem lykkjan fer.

Búðu til nýja skrá, *verkefni9.py*.


*Dæmi:*

.. code-block:: python
    
    for x in range(1, 10):
        print(x)

Hér skilgreinum við *x* innan lykkjunnar og notum aðgerðina *range()* til að skilgreina tölusvið frá 1 - 10. Við fáum 10 sæti og í hverjum hring tekur *x* gildið af sætinu.

*For* lykkjur hafa nokkrar skipanir sem við getum einnig notað.


*Dæmi:*

.. code-block:: python
    
    for x in range(1, 10):
        if x == 5:
            continue
        print(x)

Skipunina *continue* getum við notað til að sleppa öllum aðgerðum í þeim hring sem við erum í og byrja strax á næsta hring. Hér er *print(x)* aðgerðinni sleppt.


.. code-block:: python
    
    for x in range(1, 10):
        if x == 5:
            pass                
        print(x)


Skipunina *pass* er oft notuð þegar uppkast að kóða er skrifað. Ég vil að eitthvað gerist þegar *x == 5* en á eftir að skilgreina það betur.


Hér erum við að nota sett af tölum sem lykkjan fer yfir. Við getum farið yfir alls kyns tegundir af settum. Strengur er t.d. sett af stöfum. Orðið "Rafiðnaðarskólinn" hefur 17 sæti, þ.e. 1 sæti fyrir hvern staf.


*Dæmi:*

.. code-block:: python
    
    for stafur in "Rafiðnaðarskólinn":
        print(stafur)


Hver stafur hefur sætisnúmer og fyrsta sætið byrjar á 0. "R" er því í sæti 0, "a" í sæti 1 o.s.f.v. Við getum notað sætisnúmerin til að prenta út innihald sætisins. Fyrst þurfum við að skilgreina aðra breytu með aðgerðinni *enumerate()* til að gefa hverjum staf sætisnúmer.

*Dæmi:*

.. code-block:: python
    
    texti = "Rafiðnaðarskólinn"
    print(len(texti)) # prófum að prenta út fjölda sæta

    for teljari, stafur in enumerate(texti):
        print(texti[teljari])


Aðgerðin *len()* prentar út fjölda sæta en athugaðu að síðasti stafurinn í orðinu er með sætisnúmerið *16* af því að fyrsta sætið er með sætisnúmerið 0.




.. _thermo-assignment-9:
    

Verkefni 9
___________

* Finndu frétt á netinu og settu textann í breytu. Sameinaðu málsgreinar svo hann sé einn langur strengur.
* Notaðu *for* lykkju til að telja öll "r" (eða hvaða bókstaf sem er) og prentaðu út fjölda í lokin.
* Skilgreindu aðra breytu til að safna saman fjöldanum í hverjum hring.