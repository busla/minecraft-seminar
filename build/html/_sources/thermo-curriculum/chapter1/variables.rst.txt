.. _thermo-variables:

Breytur
=======


Við getum líka geymt allar aðgerðir sem við gerum í *breytum* og notað þær síðar.

>>> tugabrot = 10.9876
>>> tala = 5
>>> texti = 'Ég heiti Jón'

Breyturnar *tala* og *texti* eru núna það sama og gildið sem við gáfum þeim.

>>> tala
5
>>> texti
Ég heiti Jón

Hvað gerist ef við reynum að líma þetta saman?

>>> tala + texti
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'

Akkúrat. Við fáum villu því að breyturnar *tala* og *texti* geyma ekki sama gagnatípan. Önnur geymir heila tölu (*integer*) og hin geymir streng (*string*)

Breytum tölu í streng og prentum út. Notum aðgerðina *print()* í seinni aðgerðinni.

>>> str(tala) + texti
Ég heiti Jón.

>>> print(str(tala) + texti)


Aðgerðir (föll) geta tekið *færibreytur*. Hér erum við að senda tvær færibreytur í fallið *print()*

>>> print(tala, texti)


Hvaða gagnatípur eru þetta? Sendum breytuna *tala* sem færibreytu í fallið *type()* til að komast að því.

>>> type(tala)
<class 'int'>

>>> type(texti)
<class 'str'>

>>> type(tugabrot)
<class 'float'>

Ætli við getum reiknað með breytum?

>>> tala = 5
>>> tala + tala
10
>>> tala = 5
>>> tala * 2
10

>>> tala = 5
>>> tala = tala + tala
>>> tala
10

Við getum líka stytt okkur leið og gert:

>>> tala = 5
>>> tala += tala
>>> tala
10

Sem er það sama og:

>>> tala = tala + tala


Prentum út texta í bland við integer:
>>> nafn = "Jón Levy"
>>> simi = "7798217"
>>> print("Ég heiti {} og síminn hjá mér er {}".format(nafn, simi))

.. _thermo-assignment-3:

Verkefni 3
----------

Skiptu út tölunum í textanum fyrir skilgreindar breytur og reiknaðu út þar sem við á:

* Í dag er mánudagurinn 9. janúar og hitastigið er 7 gráður á celsíus. 
* 100 deilt með 10 eru 10
* 5.23 plús 4.77 plús 5 eru 15
