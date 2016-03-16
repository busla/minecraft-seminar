.. _our-tools:

Verkfærin okkar
===============

**Verkfæri forritunarmála**

Það má líkja forritunarmálum við smiði. Þeir nota allskyns tól og tæki til að smíða hús. Krana, gröfur, ýtur, naglabyssur, hamra og fleira. Öll þessi tól geta framkvæmt mismunandi aðgerðir. Hamarinn *hamrar* (og losar nagla), sögin *sagar*, skrúfjárnið *skrúfar*, o.s.f.v.

.. note::
    
    Í Python kallast aðgerð *function*
    

Verkfærin gera ekkert eins síns liðs. Þau þurfa eitthvað hráefni til að vinna með. Hamarinn þarf nagla, sögin þarf spítu og skrúfjárnið þarf skrúfu.

Í forritun myndi þetta líta svona út:

.. code-block:: python

    import Hamar

    hilla = Hamar.hamra(nagli)
    laus spíta = Hamar.losa(nagli)

Til að búa til *hillu* þurfum við að nota verkfærið *hamar* sem *hamrar* en þarf líka nagla til að geta hamrað eitthvað saman. Útkoman verður *hilla*. Hráefnið sem við notum er alltaf sett innan sviga á eftir aðgerðinni.

Þessa hillu getum við notað síðar til að geyma sokkana okkar, eða hvað annað sem þið viljið nota hana í.


Oft hafa tólin svo margar aðgerðir að það þarf að flokka þær í sér verkfærakassa. Smiðurinn geturu t.d. verið með nokkra mismunandi verkfærakassa eftir því hvað hann er að gera. Einn kassa fyrir allskyns tegundir af hömrum og nöglum, annan fyrir margar tegundir af skrúfjárnum og skrúfum og svo enn einn fyrir sandpappír og þjalir. Það færi allt í tóma vitleysu ef hann væri með einn stóran kassa fyrir þetta allt.

Dæmi um kóða þar sem við þurfum að sækja verkfærakistu myndi líta svona út:

.. code-block:: python

    from hamarkassi import Hamar

    hilla = Hamar.hamra(nagli)
    laus spíta = Hamar.losa(nagli)


.. note::
    
    Í Python eru verkfærakassar kallaðir *klasar (á ensku class)*.

Það sama gildir um málara. Penslar í einum kassa, lakk í öðrum, o.s.f.v.


Hvað myndi nú gerast ef smiðurinn og málarinn væru með sömu vinnustofu? Ef þeir geyma ekki kassana sína á sérstökum stað á vinnustofunni þá færi eflaust allt í vitleysu. Smiðurinn tæki kannski kassa af pennslum í staðinn fyrir kassa af hömrum.

Allt þarf að vera á sínum stað. Málarinn geymir sína kassa í einni geymslu og smiðurinn sína kassa í annari.

Kóði í forritun virkar á sama hátt. Allt þarf að vera á sínum stað. Dæmi um verkfærageymslu með verkfærakössum myndi líta svona út:

.. code-block:: python

    from smíðageymsla.hamarkassi import Hamar

    hilla = Hamar.hamra(nagli)
    laus spíta = Hamar.losa(nagli)

.. note::
    
    Í Python eru geymslur fyrir verkfærakassa kallaðar *einingar (á ensku modules)*



Python, rétt eins og önnur forritunarmál, býður upp á allskyns verkfæri sem við getum notað til að smíða forrit.

Eins og við sáum áðan þá eru reikningsaðgerðir innbyggðar í Python (samlagning, frádráttur, margföldun, deiling, o.s.f.v.).

En við gátum ekki reiknað saman heila tölu og texta. Afhverju ekki?

Heil tala og texti (einnig *strengur*) er sitthvor tegundin af hráefni.

Til að nota hráefni saman af sitthvorri gerðinni þurfum þau að vera eins. Í forritunarmálum eru aðgerðir til staðar sem sjá um að breyta einni tegund yfir í aðra.

Dæmi:

7 er heil tala en '7' (einnig hægt að nota tvöfaldar gæsalappir *"7"*) er texti. Við getum notað aðgerðina *int()*, sem merkir *integer* (á latínu *heil*), til að breyta strengnum '7' yfir í tölu.


>>> 6 + int('7')
13


Við getum einnig notað aðgerðina *str()*, sem merkir *string*, *(ísl: strengur)*, til að breyta tölunni 6 yfir í strenginn "6", og límt strengina saman.

>>> str(6) + '7'
'67'

Aðgerðirnar *int()* og *str()* eru innbyggðar aðgerðir sem eru aðgengileg þegar Python túlkurinn er ræstur.


Eins og sést þá birtist svarið strax á skjánum. Við getum líka geymt svarið ef við viljum kannski nota það síðar. Við geymum svör í *breytu*.

*Dæmi*

>>> tala = 7 + 7
>>> tala
14
>>> tala + 2
16

Python inniheldur einnig fjölda annara aðgerða sem við þurfum að sækja sérstaklega ef við viljum nota þau. Það er óþarfi að vera með aðgang að aðgerðum sem við þurfum ekki að nota og gæti tekið ansi langan tíma að ræsa túlkinn með öllum þeim aðgerðum sem hann býður upp á. Það væri t.d. ólíklegt að smiður myndi koma með gröfu til að smíða hundakofa.

Sjá lista yfir þau tól *(modules)* sem Python inniheldur: https://docs.python.org/3/library/index.html

Til að sækja þau tól sem við þurfum notum við skipunina *import*. Ef við þurfum t.d. að búa til slembitölu *(random)* þá getum við notað tólið *random*. Þar sem það er ekki innbyggt tól sækjum við það með *import*.

Tólið sjálft getur framkvæmt fjölda aðgerða. Grafa smiðsins getur t.d. farið áfram, afturábak, lyft og lækkað skóflunni o.s.f.v.

Prófum að sækja verkfærið *random* og nota *randrange* aðgerðina sem býr til slembitölu milli tveggja talna. Prófum að velja slembitölu milli 1 og 10.

Dæmi:

>>> import random
>>> random.randrange(1, 10)
7


Til að þurfa ekki að nota nafnið á verkfærinu í hvert skipti þá getum við sótt aðgerðina beint:

>>> from random import randrange
>>> randrange(1, 10)
7


.. _assignment-1:

Verkefni 1
----------

* Búðu til slembitölu á bilinu 0-10 og geymdu hana í breytu.
* Búðu til aðra slembitölu og geymdu hana í annari breytu.
* Birtu báðar slembitölurnar á skjánum.
* Leggðu saman tölurnar með því að nota breyturnar svo að samlagning þeirra birtist á skjánum.
