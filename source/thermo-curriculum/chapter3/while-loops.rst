.. _thermo-while-loops:

While lykkjur
============

lykkjur eru aðgerðir sem við notum til að fara yfir lista, orðasöfn eða aðra hluti sem geyma safn af gögnum sem við viljum nálgast. Ef við þyrftum t.d. að leita að nafni í símaskránni þá myndum við eflaust nota lykkjur. Einnig er hægt að nota lykkjur sem endurtaka sig þar til einhverju skilyrði er mætt.

Oftast notum við tvær tegundir af lykkjum, *while* eða *for* lykkjur. Í þessum kafla förum við í *while* lykkjur.

Búið til nýja skrá og nefnið hana *verkefni8.py*.

.. code-block:: python
    
    teljari = 0

    while teljari < 10:
        print(teljari)
        teljari = teljari + 1

Í þessum kóða búum við til breytuna *teljari*. Við gefum henni gildið *0* og er því breytan af tegundinni *integer* (heil tala). Þýðum nú lykkjuna yfir á mannamál.

*Á meðan* teljari er minni en talan *10*, prentaðu út teljarann og hækkaðu svo teljarann um *1*.

Hér er önnur leið til að leggja saman teljarann:

.. code-block:: python
    
    teljari = 0

    while teljari < 10:
        print(teljari)
        teljari += 1

Þessi aðgerð endurtekur sig svo lengi sem teljari er minni en einn. Það sem *while* aðgerðin er að gera er að endurtaka sig svo lengi sem eitthvað er *satt*. Um leið og það verður *rangt* þá stoppar aðgerðin.

Við gætum t.d. gert:

.. code-block:: python
    
    import time

    while True == True:
        print('endurtekningin endalausa')
        time.sleep(1)

Á meðan *satt* er *satt* prentaðu textann og farðu að sofa í 1 sekúndu. Ef þú vilt framkvæma einhverja aðgerð í ákveðin tíma þá gæti hentað ágætlega að nota *while* lykkju og nota aðgerðina *sleep()* til að ákveða tímalengdina.

Hvað myndi gerast hér? Þessi lykkja myndi aldrei hætta því samanburðurinn breytist aldrei, *satt* verður alltaf *satt*.

.. note::
    
    Ýttu á CTRL+C til að stöðva lykkjuna.

Þótt þetta líti út fyrir að vera tilgangslaust þá eru tilfelli þar sem við getum nýtt okkur endalausa lykkju. Til að stöðva lykkjuna notum við skipunina *break*.

*Dæmi*

.. code-block:: python

    i = 1

    while True: # gerir það sama og *while True == True*
        
        print('Þessi texti mun endurtaka sig 10 sinnum')
        
        if i == 10:
            break

        i += 1

Í hvert skipti sem lykkjan endurtekur sig er athugað hvort breytan *i* sé með gildið *10*. Ef hún er það ekki skaltu hækka *i* um einn.


Í síðasta kafla þá lentum við í vandræðum þegar notandinn sló inn bókstafi í stað talna. Lögum það með því að setja *input()* í lykkju.


.. code-block:: python
    while True:
        x = input('Sláðu inn hita í °F: ')

        try:
            celsius = (float(x) - 32) / 1.8 # T(°C) = (T(°F) - 32) / 1.8
        except ValueError as error: # geymum villuna í breytunni error
            print('Aðeins tölur eru leyfðar. Fékk villuna {}'.format(error))
        else:            
            print("Hitinn er {}°C".format(round(celsius, 2)))
            break


.. _thermo-assignment-8:
    

Verkefni 8
___________

Undantekningar (exceptions) hafa eina skipun í viðbót. Notaðu Google til að finna hana og finndu not fyrir hana í kóðanum hér fyrir ofan.
