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

Þessi aðgerð skilar okkur niðurstöðum. Við biðjum Minecraft að kíkja hvar hann er og senda okkur tilbaka staðsetninguna. Hvernig geta þessar þrjár tölur verið staðsetningin hans? Málið er að þetta er staðsetningin hans í hnitum. Til að finna staðsetningu í hnitum skulum við skoða herbergið sem við erum í. Allt inni í herberginu hefur einhverja staðsetningu. Myndin á veggnum, stóllinn, tölvan, allt sem þú sérð. Til að átta okkur betur á hnitum getum við ímyndað okkur taflborð. Taflborðið er merkt með bókstöfum á einni hlið og tölustöfum á hinni. Ef við skoðum t.d. hvíta hrókinn vinstra meginn þá hefur hann hnitið A,1. Hann getur farið til hliðar eftir tölustöfum (x ás) og áfram eftir bókstöfum (y ás). Við notum orðið *ás* þegar við tölum um áttir. Ef við setjum hann einhverstaðar á borðið þá getum við séð hnitið hans með því að skoða töluna og bókstafinn sem hann er á. 

Vandamálið með taflið er að taflmennirnir geta bara farið áfram og til hliðar á borðinu. Þeir geta ekki farið upp í loft sem er þriðji ásinn og við skulum kalla hann *z ás*. Þegar við erum með þrjú hnit þá getum við kallað það þrívídd. Taflborðið væri þá tvívídd. Miðað við röðunina *x, y, z* þá væri bolur sem liggur á gólfinu í vinstra horninu á herberginu með hnitið *0, 0, 0*. Ef við myndum setja hann upp á lítið borð í sama horni þá væri hann hugsanlega með hnitið *0, 0, 2* því hann hefur hækkað.


En aftur að Steve. Hann er staddur einhverstaðar í Minecraft heiminum ykkar og við getum fengið að vita nákvæmlega hvar hann er með því að skoða *x, y, z* hnitið hans.

Við getum meira að segja geymt hnitin hans í breytum og notað síðar. Af því að aðgerðin :attr:`~minecraft.CmdPlayer.getPos` skilar okkur þremur tölum þá skulum við nota þrjár breytur til að geyma þær í sitthvoru lagi.


*Dæmi*

>>> from mcpi.minecraft import Minecraft
>>> mc = Minecraft.create()
>>> mc.player.getPos()
Vec3(1.9, 5.4, 9.8)
>>> player = mc.player.getPos()
>>> player.x
5.6
>>> player.y
9.1
>>> player.z
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







