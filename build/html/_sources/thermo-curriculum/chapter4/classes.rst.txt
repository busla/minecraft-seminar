.. _thermo-classes:

Klasar (classes)
=================

Það er gott að hugsa um :ref:`thermo-dictionaries` þegar við lærum um klasa. Gildi eru geymd í hólfum sem hafa eitthvað nafn.
Hér er gildið *"Jón Levy"* geymt í hólfinu *"nafn"*. Breytan *safn* getur svo haft mörg mismunandi hólf.

.. code-block:: python
    
    safn = {'nafn': 'Jón Levy'}
    print(safn['nafn'])


Þá má hugsa um klasa sem samansafn af föllum og breytum sem við notum með heilstæðum hætti. Klasinn sjálfur gerir hins vegar ekki neitt heldur er hann teikning (samanber teikning af húsi) sem er hægt að nota til að framkvæma aðgerðir. Hann er síðan notaður til að búa til hluti, rétt eins og hægt er að nota sömu teikningu af húsi til að smíða mörg stök af húsinu.

Húsið hefur eiginleika (properties). Það hefur lit, hæð, breidd, fjölda glugga, fjölda herbergja o.s.f.v.

Hægt er að framkvæma aðgerðir á húsinu (methods/functions). Það er hægt að *opna()* hurðir og glugga, *mála()* veggina, *kveikja-á-ofnum()*, o.s.f.v.

Skilgreinum nú teikningu af húsi. Búðu til skrána *verkefni13.py*.

.. code-block:: python

    class House(object):

        def __init__(self, color, doors, windows, height, length):
            self.color = color
            self.doors = doors
            self.windows = windows
            self.length = length

        def paint(self, color):
            self.color = color
            print('Húsið hefur fengið nýjan lit: {}'.format(self.color))
            return


        def add_window(self, num):
            self.windows += num
            print('Við bættum við glugga, nú eru þeir {}'.format(self.windows))
            return 


    h1 = House('rauður', 2, 10, 25, 10)
    h2 = House('blár', 5, 2, 50, 7)
    h3 = House('grænn', 3, 100, 40, 4)
    print(h1)
    print(h2)
    print(h3)


    h1.paint('blár')
    h2.add_window(2)


Þessi klasi hefur tvö föll, *paint()* og *add_window()*. Athugaðu að við notum ekki orðið *fall* þegar við skilgreinum aðgerðir í klösum, heldur *aðferð* *(method)*. Ástæðan fyrir þessu er sú að innan sama kóða getum við verið að nota föll sem eru ekki hluti af klösum og svo aðferðir sem eru hluti af klösum. Föll og aðferðir gera nákvæmlega það sama. Taka inn færibreytur og skila einhverri niðurstöðu. Það sem aðferðir gera hins vegar er að breyta eingöngu stakinu sem var búið til.

Í kóðanum fyrir ofan kölluðum við í:


.. code-block:: python
    
    #....

    h1.paint('blár')


Þetta breytir ekki litnum á *h2* né *h3* stakinu. Aðferðir í klösum eru eingöngu keyrðar á stakinu sem kallar í þær.

Efst í klasanum er aðferð sem nefnist *__init__()*. Allir klasar hafa þessa aðferð því í hana er kallað um leið og stak er búið til. Þegar við bjuggum til *h1*, *h2* og *h3* stökin þá var kallað í *__init__()*. Þar skilgreinum við einnig færibreytur sem við viljum nota sem eiginleika.

Í *__init__()* fallinu vistum við svo gildin úr færibreytunum í nýjum breytum sem við setjum *self* fyrir framan. Það vísar í stakið sem verið er að búa til. Þessar *self* breytur getum við svo notað hvar sem er í stakinu.

Þegar við skilgreinum klasa þá er gott að geyma þá í sér skrá. Búðu til skrána *house.py* og settu klasann þangað inn. Restina skaltu geyma í *verkefni13.py*.


.. code-block:: python

    class House(object):

        def __init__(self, color, doors, windows, height, length):
            self.color = color
            self.doors = doors
            self.windows = windows
            self.length = length

        def paint(self, color):
            self.color = color
            return 'Húsið hefur fengið nýjan lit: {}'.format(self.color)


        def add_window(self, num):
            self.windows += num
            return 'Við bættum við glugga, nú eru þeir {}'.format(self.windows)            



Efst í *verkefni13.py* skaltu sækja *House* klasann með *import* skipuninni. Skoðaðu :ref:`thermo-our-tools` til upprifjunar.

.. code-block:: python

    # settu import skipun hér.

    h1 = House('rauður', 2, 10, 25, 10)
    h2 = House('blár', 5, 2, 50, 7)
    h3 = House('grænn', 3, 100, 40, 4)
    print(h1)
    print(h2)
    print(h3)


    print(h1.paint('blár'))
    print(h2.add_window(2))


.. _thermo-assignment-13:
    
Verkefni 13
____________

* Opnaðu :ref:`thermo-assignment-12` og afritaðu kóðann í skrána *hitakerfi.py*
* Notaðu föllin í kóðanum sem aðferðir í klasa sem þú skilgreinir
* Í skránni *verkefni13.py* skaltu nota *import* skipunina til að sækja klasann og búa til nokkur hitastök. 