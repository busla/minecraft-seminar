.. _input:

Inntak
======

Til að senda Steve á nýjan stað þá þurfum við að endurræsa kóðann okkar í hvert skipti.

Hvað ef við gætum bara stimplað inn tölur á skjánum og Steve fer svo af stað? Það er lítið mál. Við notum aðgerðina *input* til þess að bjóða upp á innslátt. Búið fyrst til nýja skrá og nefnið hana *verkefni6.py*. 

*Dæmi*

.. code-block:: python

    from mcpi.minecraft import Minecraft

    mc = Minecraft.create()
    innslattur = input('Sláðu inn texta: ')
    print(innslattur)

Aðgerðin *input()* er innbyggð í Python. Hún sendir texta á skjáinn og bíður eftir að notandinn slái inn gildi. Þegar breytan *innslattur* hefur fengið gildi frá notandanum heldur forritið okkar áfram og prentar út gildið. Við getum beðið notandann um að slá nokkur gildi.


*Dæmi*

.. code-block:: python

    from mcpi.minecraft import Minecraft

    mc = Minecraft.create()
    x = input('Sláðu inn gildi fyrir x: ')
    y = input('Sláðu inn gildi fyrir y: ')
    z = input('Sláðu inn gildi fyrir z: ')

    print(x, y, z)

Þessi gildi getum við svo notað til að framkvæma þær aðgerðir sem við viljum. Prófum að senda Steve á hnit sem notandinn slær inn. Passið ykkur að hafa gildin ekki stærri en *127* því Minecraft heimurinn er ekki endalaus.

*Dæmi*

.. code-block:: python

    from mcpi.minecraft import Minecraft

    mc = Minecraft.create()
    x = input('Sláðu inn gildi fyrir x: ')
    y = input('Sláðu inn gildi fyrir y: ')
    z = input('Sláðu inn gildi fyrir z: ')

    print(x, y, z)

    mc.player.setPos(x, y, z)


Afhverju fengum við villu?

Öll gildi sem við sláum inn er *strengur*. Ef við viljum nota þau í t.d. útreikningum þá þurfum við að breyta strengnum í *integer* (heila tölu) eða *float* (brotatölu). Í skilgreiningunni á :meth:`~minecraft.CmdPlayer.setPos` kemur fram að aðgerðin tekur brotatölu. Ástæðan fyrir því að við getum líka notað heila tölu er sú að Python 3 breytir *integer* yfir í *float* ef þess er krafist. Það gengur hins vegar ekki í hina áttina, þ.e., það er ekki hægt að breyta *float* yfir í *integer* án þess að nota aðgerðir sem t.d. námunda brotatöluna upp eða niður.

En áfram með smjörið. Breytum strengnum yfir í tölu.


*Dæmi*

.. code-block:: python

    from mcpi.minecraft import Minecraft

    mc = Minecraft.create()
    x = input('Sláðu inn gildi fyrir x: ')
    y = input('Sláðu inn gildi fyrir y: ')
    z = input('Sláðu inn gildi fyrir z: ')

    print(x, y, z)

    mc.player.setPos(int(x), int(y), int(z))

Við getum líka breytt strengnum á öðrum stað.

*Dæmi*

.. code-block:: python

    from mcpi.minecraft import Minecraft

    mc = Minecraft.create()
    x = int(input('Sláðu inn gildi fyrir x: '))
    y = int(input('Sláðu inn gildi fyrir y: '))
    z = int(input('Sláðu inn gildi fyrir z: '))

    print(x, y, z)

    mc.player.setPos(x, y, z)

Þetta lítur flókið út. Fullt af svigum. Eins og í almennum reikningi þá byrjum við fyrst að reikna út gildin í innsta sviganum og finnum okkur út á við. Við byrjum á að fá gildið frá notandanum og breytum því svo í *integer* áður en breytan *x* fær gildið.

Bætum við annari aðgerð til að flækja hlutina enn meira.

*Dæmi*

.. code-block:: python

    from mcpi.minecraft import Minecraft

    mc = Minecraft.create()
    x = float(int(input('Sláðu inn gildi fyrir x: ')))
    y = float(int(input('Sláðu inn gildi fyrir y: ')))
    z = float(int(input('Sláðu inn gildi fyrir z: ')))

    print(x, y, z)

    mc.player.setPos(x, y, z)

Fyrst fáum við strenginn, breytum honum í heila tölu og svo í brotatölu. Það er lítill tilgangur með þessu því að heila talan *7* breytist einfaldlega í *7.0*.

.. _assignment-6:

Verkefni 6
----------
* Spurðu notandann hvort hann vilji senda Steve á nýja hnitið. Ef hann vill það ekki þá fer hann ekki neitt. Skoða vel :ref:`if-else`.
