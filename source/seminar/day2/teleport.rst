Teleport
===============

Oft viljum við einnig nota tól sem eru ekki innifalin í Python. Minecraft Pi tólin eru ekki hluti af Python safninu og því þurfum við að sækja þau sérstaklega þegar við skrifum kóða.

Minecraft tólin hafa fjölda aðgerða sem við getum leikið okkur með.

Ef við kíkjum á :doc:`../minecraft-api` þá sjáum við listann yfir klasana og aðgerðirnar sem þeir hafa. Það fyrsta sem við ætlum að gera er að skoða aðgerðina :attr:`~minecraft.CmdPlayer.getPos` sem sækir staðsetninguna á Steve.

Í stað þess að skrifa þetta í Python skelinni skulum við opna *Python (IDLE3)* forritið og búa til nýja skrá *(File -> New file)*. Vistiði hana síðan sem *verkefni3.py* í möppunni *pi*. Þetta verður fyrsta forritið sem við búum til fyrir Minecraft. Það eina sem forritið okkar gerir er að segja okkur hvar Steve er staðsettur.


*Dæmi*

>>> from mcpi.minecraft import Minecraft
>>> mc = Minecraft.create()
>>> mc.player.getPos()
Vec3(34.6, 29.9, -18.1)

Þessi aðgerð skilar okkur einum hlut af tegundinni *Vec3* sem hefur þrjá eiginleika sem er hnitið á staðsetningu Steve.
 

Til að finna hnit hlutar skulum við skoða herbergið sem við erum í. Allt inni í herberginu hefur einhverja staðsetningu. Myndin á veggnum, stóllinn, tölvan, allt sem þú sérð. Til að átta okkur betur á hnitum getum við ímyndað okkur taflborð. Taflborðið er merkt með bókstöfum á einni hlið og tölustöfum á hinni. Ef við skoðum t.d. hvíta hrókinn vinstra meginn þá hefur hann hnitið A,1. Hann getur farið til hliðar eftir tölustöfum (z ás) og áfram eftir bókstöfum (x ás). Við notum orðið *ás* þegar við tölum um áttir. Ef við setjum hann einhverstaðar á borðið þá getum við séð hnitið hans með því að skoða töluna og bókstafinn sem hann er á. 

Vandamálið með taflið er að taflmennirnir geta bara farið áfram og til hliðar á borðinu. Þeir geta ekki farið upp í loft sem er þriðji ásinn og við skulum kalla hann *y ás*. Þegar við erum með þrjá punkta þá getum við kallað það þrívídd. Taflborðið væri þá tvívídd. Miðað við röðunina *x, y, z* þá væri bolur sem liggur á gólfinu í vinstra horninu á herberginu með hnitið *0, 0, 0*. Ef við myndum setja hann upp á lítið borð í sama horni þá væri hann hugsanlega með hnitið *0, 2, 0* því hann hefur hækkað.


En aftur að Steve. Hann er staddur einhverstaðar í Minecraft heiminum ykkar og við getum fengið að vita nákvæmlega hvar hann er með því að skoða *x, y, z* hnitið hans.

Það sem við fáum frá *getPos()* er einn hlutur með þrjá eiginleika, *x, y, z* hnitin á Steve. Þegar aðgerðir skila okkur hlutum tilbaka þá getum við notað eiginleika þeirra. Hlutur getur verið með hvaða eiginleika sem er. Peysa gæti t.d. haft eiginleikana *litur, efni, þykkt, stærð*. Til að nálgast eiginleika hluta í Python notum við heitið á þeim.


Við getum líka geymt hnitið hans í breytum og notað síðar. Af því að aðgerðin :attr:`~minecraft.CmdPlayer.getPos` skilar okkur hlut með þremur punktum þá skulum við nota þrjár breytur til að geyma þær.


*Dæmi*

>>> from mcpi.minecraft import Minecraft
>>> mc = Minecraft.create()
>>> mc.player.getPos()
Vec3(1.9, 5.4, 9.8)
>>> hnit = mc.player.getPos()
>>> hnit.x
1.9
>>> hnit.y
5.4
>>> player.z
9.8


En hvað getum við gert við þetta hnit? Ef við kíkjum aftur í :doc:`../minecraft-api` þá sjáum við að það eru fleiri aðgerðir sem við getum notað, eins og :meth:`~minecraft.CmdPlayer.setPos` þar sem við sendum hnit inn í leikinn og Steve fer beint á hnitið. Gildi sem við sendum í aðgerðina kallast *færibreytur*. Í þessari aðgerð hefur aðgerðin :meth:`~minecraft.CmdPlayer.setPos` þrjár færibreytur, *x, y, z*.

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







