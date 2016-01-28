Python skelin
=============

**Hvað er Python?**

.. todo::
    texti um python


*Opna Terminal*

Fariði í forritið *Terminal* og skrifið:

.. code-block:: bash

    $ python3

    Python 3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 00:54:21) 
    [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

Nú eruði kominn í Python skelina. Allur Python kóði sem þið skrifið verður túlkaður um leið. 

**Heilar tölur**

>>> 8
8

>>> 1 + 1
2

>>> 5 * 9
45

**Texti**

>>> 'þetta er texti'
þetta er texti

>>> 'þetta' + ' er ' + 'texti'
þetta er texti

**Texti og tölur**

Hvað ef við notum tölur og texta saman?

>>> 5 + "9"
TracebackError

Við fáum villu.


Breytur
_______

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

Akkúrat. Við fáum villu því að breyturnar *tala* og *texti* geyma ekki sama hráefnið. Önnur geymir heila tölu (*integer*) og hin geymir streng (*string*)

En.. hvað ef við breytum *tala* í streng?

>>> str(tala) + texti
5Ég heiti Jón.

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




