.. _thermo-input:

Inntak
======

Aðgerðin *input()* er innbyggð í Python. Hún tekur texta sem færibreytu og bíður eftir að notandinn slái inn gildi. Þegar breytan *innslattur* hefur fengið gildi frá notandanum heldur forritið okkar áfram.


*Dæmi*

.. code-block:: python


    x = input('Sláðu inn hita í celsíus: ')
    fahrenheit = x * 1.8 + 32
    print(fahrenheit)

.. code-block:: python


    Traceback (most recent call last):
      File "verkefni5.py", line 3, in <module>
        fahrenheit = x * 1.8 + 32
    TypeError: can't multiply sequence by non-int of type 'float'


Afhverju fengum við villu?

Öll gildi sem við sláum inn er *strengur*. Python breytir ekki texta yfir í tölu sjálfkrafa þótt við sláum inn tölustafi. Ef við viljum nota strenginn í t.d. útreikningum þá þurfum við að breyta strengnum í *integer* (heila tölu) eða *float* (brotatölu). Við skulum breyta strengnum í *float* ef notandinn skyldi slá inn brotatölu.

Áfram með smjörið. Breytum strengnum yfir í tölu og bætum við betri lýsingu í úprentun.


*Dæmi*

.. code-block:: python


    x = input('Sláðu inn hita í celsíus: ')
    fahrenheit = float(x) * 1.8 + 32 # T(°F) = T(°C) × 1.8 + 32
    print("Hitinn er {} í fahrenheit".format(fahrenheit))


Til að sleppa við óþarflega marga aukastafi þá getum við stjórnað fjöldanum með *round()* aðgerðinni.

.. code-block:: python


    x = input('Sláðu inn hita í °C: ')
    fahrenheit = float(x) * 1.8 + 32
    print("Hitinn er {}°F".format(round(fahrenheit, 2)))


Snúum þessu nú við og breytum °F í °C

.. code-block:: python


    x = input('Sláðu inn hita í °F: ')
    celsius = (float(x) - 32) / 1.8 # T(°C) = (T(°F) - 32) / 1.8
    print("Hitinn er {}°C".format(round(celsius, 2)))


Hvað ef ég slæ bókstafi inn í staðinn fyrir tölur? Prófum að slá inn "veit það ekki".

.. code-block:: python

    Traceback (most recent call last):
      File "testing.py", line 2, in <module>
        celsius = (float(x) - 32) / 1.8 # T(°C) = (T(°F) - 32) / 1.8
    ValueError: could not convert string to float: 'veit það ekki'


Við fáum við villuna`ValueError` því að textinn inniheldur ekki tölur og ómögulegt að breyta honum yfir í *float*.

Í Python er hægt að reyna að gera hluti og biðjast fyrirgefninar ef það tekst ekki, svokölluð *undantekning* (exception), til að koma í veg fyrir að forritið brotni ekki í sundur.


.. code-block:: python

    x = input('Sláðu inn hita í °F: ')

    try:
        celsius = (float(x) - 32) / 1.8 # T(°C) = (T(°F) - 32) / 1.8
        print("Hitinn er {}°C".format(round(celsius, 2)))    
    except ValueError:
        print('Aðeins tölur eru leyfðar')


Við getum líka bætt við *else* í lokin sem verður eingöngu keyrt ef *try* aðgerðin gengur upp:


.. code-block:: python

    x = input('Sláðu inn hita í °F: ')

    try:
        celsius = (float(x) - 32) / 1.8 # T(°C) = (T(°F) - 32) / 1.8
    except ValueError:
        print('Aðeins tölur eru leyfðar')
    else:
        print("Hitinn er {}°C".format(round(celsius, 2)))    


En forritið okkar stöðvast ef við sláum inn bókstafi. Myndum við ekki vilja láta forritið endurtaka beiðnina um að slá inn tölur ef notandinn slær inn bókstafi?

Við leysum það vandamál í kaflanum um *lykkjur*

.. _thermo-assignment-7:

Verkefni 7
----------

* Skilgreindu tvær breytur sem taka við innslætti frá notanda. Önnur breytan tekur við hita og hin tekur bókstafinn *C* eða *F*.
* Notaðu *if/else* til að athuga hvort eigi að breyta úr celsíus í fahrenheit eða öfugt.