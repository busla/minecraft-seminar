While lúppur
============

Lúppur eru aðgerðir sem við notum til að spóla í gegnum lista, orðasöfn eða aðra hluti sem geyma safn af gögnum sem við viljum nálgast. Ef við þyrftum t.d. að leita að nafni í símaskránni þá myndum við eflaust nota lúppur.

Oftast notum við tvær tegundir af lúppum, *while* eða *for* lúppur. Í þessum kafla förum við í *while* lúppur.

Búið til nýja skrá og nefnið hana *verkefni10.py*.

.. code-block:: python
    
    teljari = 0

    while teljari < 10:
        print(teljari)
        teljari += 1

Í þessum kóða búum við til breytuna *teljari*. Við gefum henni gildið *0* og er því breytan af tegundinni *integer (heil tala)*. Þýðum nú lúppuna yfir á mannamál.

*Á meðan* teljari er minni en talan *10*, prentaðu út teljarann og hækkaðu svo teljarann um *1*.

Þessi aðgerð endurtekur sig svo lengi sem teljari er minni en einn. Það sem *while* aðgerðin er að gera er að endurtaka sig svo lengi sem eitthvað er *satt*. Um leið og það verður *rangt* þá stoppar aðgerðin.

Við gætum t.d. gert:

.. code-block:: python
    
    import time

    while True == True:
        print('endurtekningin endalausa')
        time.sleep(1)

Á meðan *satt* er *satt* prentaðu textann og farðu að sofa í 1 sekúndu. Ef þú vilt framkvæma einhverja aðgerð í ákveðin tíma þá gæti hentað ágætlega að nota *while* lúppu og nota aðgerðina *sleep()* til að ákveða tímalengdina.

Hvað myndi gerast hér? Þessi lúppa myndi aldrei hætta því samanburðurinn breytist aldrei, *satt* verður alltaf *satt*.

.. note::
    
    Ýttu á CTRL+C til að stöðva lúppuna.

Þótt þetta líti út fyrir að vera tilgangslaust þá eru tilfelli þar sem við getum nýtt okkur endalausa lúppu. Til að stöðva lúppuna notum við skipunina *break*.

*Dæmi*

.. code-block:: python

    i = 1

    while True: # gerir það sama og *while True == True*
        
        print('Þessi texti mun endurtaka sig 10 sinnum')
        
        if i == 10:
            break

        i += 1

Í hvert skipti sem lúppan endurtekur sig er athugað hvort breytan *i* sé með gildið *10*. Ef hún er það ekki skaltu hækka *i* um einn.

.. todo::

    Athuga á Pi


Búum núna til einfaldan leik í Minecraft sem lætur okkur vita þegar við sláum í blokk.

Til að fá upplýsingum um höggin notum við :meth:`~minecraft.CmdEvents.pollBlockHits` sem skilar tilbaka lista með upplýsingum um hvert högg. Í hverju sæti eru 5 gildi. 

* Tegund aðerðarinnar (HIT)
* Hnitin (x, y, z)
* Hvaða hlið var slegið á.

*Dæmi*

.. code-block:: python
    
    [
        BlockEvent(BlockEvent.HIT, 8, 17, 121, 2),
        BlockEvent(BlockEvent.HIT, -45, 20, -78, 1)
    ]    

Í hverju sæti er því eitt eintak af klasanum *BlockEvent* með upplýsingunum sem minnst var á hér fyrir ofan. Við tölum um klasa og afrit síðar. Það sem við þurfum að taka vel eftir er að þetta er listi sem geymir einhvern fjölda af hlutum.

Í lokin notum við aðgerðina :meth:`~minecraft.CmdEvents.clearAll` til að hreinsa teljarann.

Búðu til skrá með heitið *verkefni10.py* og settu inn eftirfarandi kóða. Keyrðu síðan kóðann í *Terminal*.

.. code-block:: python

    from mcpi.minecraft import Minecraft
    from time import sleep

    mc = Minecraft.create()

    while True:
        
        hogg = len(mc.events.pollBlockHits())    
        
        if hogg > 0:
            print('Þú slóst %d sinni í blokk' % hogg)
            mc.events.clearAll()
        
        sleep(0.5)


Athugið að breytan *hogg* er listi og við getum athugað lengdina á listanum til að vita hversu oft var slegið í blokk. Í leiknum okkar er lúppan svæfð í 500 millisekúndur eftir hvern hring.

Í leiknum okkar sjáum við nýja aðferð við að prenta út upplýsingar í Terminal. Við setjum *%d (decimal, ísl: tugabrot)* inn í miðjan textann okkar og sendum svo tölu gildi þangað inn breytunni *hogg*. 

Við getum líka notað *%s* til að prenta út streng en þá þurfum við fyrst að breyta tölunni í streng.

print('Þú slóst %s sinni í blokk' % str(hogg))

Önnur leið við að prenta út það sama væri:

>>> print('Þú slóst ' + str(hog) + ' sinni í blokk')


.. _assignment-10:
    
Verkefni 10
___________

* Búðu til leik sem telur hversu oft Steve nær að slá í blokk á 10 sekúndum

Svona myndi hluti kóðans líta út á mannamáli.

Lúppan endalausa hefst. Ef það eru högg í listanum sem við fáum frá *pollBlockHits()* hækkaðu breytuna *teljari* um einn.

