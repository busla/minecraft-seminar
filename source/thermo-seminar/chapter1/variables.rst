Breytur
=============


Við getum líka geymt allar aðgerðir sem við gerum í *breytum* og notað þær síðar.

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

En.. hvað ef við breytum *tala* í streng?

>>> str(tala) + texti
Ég heiti Jón.

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
