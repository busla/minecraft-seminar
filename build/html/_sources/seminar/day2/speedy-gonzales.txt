Speedy Gonzales
===============

Minecraft klasarnir hafa fjölda aðgerða sem við getum leikið okkur með. Við erum búinn að prófa að senda skilaboð á skjáinn en hvað getum við látið Steve gera?

Ef við kíkjum á :doc:`../minecraft-api` þá sjáum við listann yfir klasana og aðgerðirnar sem þeir hafa. Það fyrsta sem við ætlum að gera er að skoða aðgerðina :attr:`~minecraft.CmdPlayer.getPos` sem sækir staðsetninguna á Steve.

*Dæmi*

>>> from mcpi.minecraft import Minecraft
>>> mc = Minecraft.create()
>>> mc.player.getPos()

.. todo::
    
    Vantar dæmi um hnitaniðurstöður

Þessi aðgerð skilar okkur niðurstöðum. Við biðjum Minecraft að kíkja hvar hann er og senda okkur tilbaka staðsetninguna. Hvernig geta þessar þrjár tölur verið staðsetningin hans? Málið er að þetta er staðsetningin hans í hnitum. Til að finna staðsetningu í hnitum skulum við ímynda okkur taflborð. Við getum fundið staðsetninguna á vinstri riddaranum með því að telja reitina til hliðar og áfram. Muniði þegar við vorum að tala um breytur? Hnit geta hafa breyturnar x, y (einnig z, sjá síðar) og innihald þeirra er fjarlægðin frá neðstu hliðinni og vinstri hliðinni.

Ef við byrjum á 0 og teljum reitina meðfram hliðinni sem snýr að okkur þá fáum við eftirfarandi fjarlægðir:

* Hrókur = 1
* Riddari = 2
* Biskup = 3
* Kóngur = 4
* Drottning = 5
* Biskup = 6
* Riddari = 7
* Hrókur = 8

Þetta eru hnit taflmannana á x ás. Hver væru hnit þeirra á y ás? Þá þyrftum við að telja áfram, meðfram vinstri hliðinni.

* Hrókur = 1
* Riddari = 1
* Biskup = 1
* Kóngur = 1
* Drottning = 1
* Biskup = 1
* Riddari = 1
* Hrókur = 1

Hmm, þetta er eitthvað skrítið. Þeir eru allir með sama hnitið? Það er af því að þeir eru allir með sömu hæðarlínu. Reynum aftur með peðið lengst til hægri.

Peðið lengst til hægri er með x ásinn 8 og y ásinn 2.

Þegar við notum riddarann þá þurfum við stundum að hoppa yfir aðra leikmenn. Þá lyftum við riddaranum af borðinu. Þegar við lyftum honum upp þá breytist hæðin á honum og annað hnit bætist við, y, sem er notað fyrir hæð.

Þannig getum við fundið nákvæma staðsetningu á hlutum í kringum okkur. Tannburstinn ykkar er t.d. með ákveðið x,z,y hnit á heimilinu.

En aftur að Steve. Hann er staddur einhverstaðar í Minecraft heiminum ykkar og við getum fengið að vita nákvæmlega hvar hann er með því að skoða x, y, z hnitið hans.

Við getum meira að segja geymt hnitin hans í breytum og notað síðar. Af því að aðgerðin getPos skilar okkur þremur tölum þá skulum við nota þrjár breytur til að geyma þær í sitthvoru lagi.


*Dæmi*

>>> from mcpi.minecraft import Minecraft
>>> mc = Minecraft.create()
>>> mc.player.getPos()
Vec3(1.9, 5.4, 9.8)
>>> player = mc.player.getPos()
>>> player.x
5.6
>>> y
9.1
>>> z
2.3


En hvað getum við gert við þessi hnit? Ef við kíkjum aftur í :doc:`../minecraft-api` þá sjáum við að það eru fleiri aðgerðir sem við getum notað, eins og :meth:`~minecraft.CmdPlayer.setPos` þar sem við sendum hnit inn í leikinn og Steve fer beint á hnitið. Gildi sem við sendum í aðgerðina kallast *færibreytur*. Í þessari aðgerð hefur aðgerðin :meth:`~minecraft.CmdPlayer.setPos` þrjár færibreytur, *x, y, z*.

*Dæmi*

>>> from mcpi.minecraft import Minecraft
>>> mc = Minecraft.create()
>>> mc.player.setPos(4, 5, 6)

Skemmtilegt. Við getum fært hann eins og við viljum! Passið ykkur samt, því ef hnitið er inni í fjalli þá festist hann og þið þurfið að fara úr leiknum til að byrja upp á nýtt.

Væri ekki gaman að stjórna því betur hvert hann færi?


.. _assignment-3:

Verkefni 3
----------
* Sæktu staðsetningun á Steve og settu hana í breyturnar *x, y, z*
* Færðu Steve áfram á *y* ás um 5 hnit
* Færðu Steve til vinstri á *x* ás um 10 hnit
* Færðu Steve upp í loft á *z* ás um 30 hnit







