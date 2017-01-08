.. _thermo-functions:

Föll (functions)
=================

Fall er safn af skipulögðum og endurnýjanlegum kóða sem er notaður til að framkvæma eina eða fleiri aðgerðir.

Búðu til skrána *verkefni12.py*.

.. code-block:: python

    def prenta_texta():
        print('Það er kalt úti')

    prenta_texta()


Við höfum verið að nota *föll* (stundum kallað *aðgerðir*) í öllu námsefninu. Python gefur okkar aðgang að fjölda falla en stundum þurfum við að sækja módúlurnar sérstaklega, t.d. *random*.


Föll geta líka tekið eina eða fleiri færibreytur sem eru aðskildar með kommu.

.. code-block:: python

    def prenta_texta(texti1, texti2):
        print(texti1)
        print(texti2)

    prenta_texta('Það er kalt úti', 'hitinn er aðeins 2 gráður')



.. code-block:: python

    def prenta_texta(texti1, texti2):
        print(texti1)
        print(texti2)

    t1 = 'Það er kalt úti'
    t2 = 'hitinn er aðeins 2 gráður'
    
    prenta_texta(t1, t2)


Við getum líka sent fall í annað fall.


.. code-block:: python

    def fall(texti):
        print(texti)

    def prenta_texta(f, texti):
        f('Það er kalt úti')
        print(texti)


    prenta_texta(fall, 'Ég þarf að fara í peysu')


Í stað þess að prenta út texta í fallinu sjálfu þá getum við látið fallið skila okkur niðurstöðum sem við notum síðar.


.. code-block:: python

    def reikna_celsius(hiti):
        return hiti * 1.8 + 32

    def reikna_fahrenheit(hiti):
        return (hiti - 32) / 1.8


    print(reikna_celsius(100))
    print(reikna_fahrenheit(100))


Stór og flókin föll sem framkvæma margar aðgerðir er erfitt að lesa. Mörg föll sem hvert fyrir sig framkvæmir eina aðgerð og gerir það vel er bæði lesanlegri og gerir okkur mun auðveldar fyrir að finna villur. Þær verða einnig endurnýtanlegri þar sem þú gætir þurft á einni ákveðinni aðgerð að halda síðar. Ef mörgum aðgerðum er blandað saman í sama fallið er ólíklegra að þú getir endurnýtt fallið annars staðar í kóðanum.


*Dæmi:*

.. code-block:: python

    def reikna_hitastig(hiti, tegund):

        if tegund == 'f':
            return hiti * 1.8 + 32
        elif tegund == 'c':
            return (hiti - 32) / 1.8
        else:
            return 'Óþekkt hitategund: "{}"'.format(tegund)


    print(reikna_hitastig(100, 'c'))


.. code-block:: python


    def reikna_celsius(hiti):
        return hiti * 1.8 + 32

    def reikna_fahrenheit(hiti):
        return (hiti - 32) / 1.8

    def reikna_hitastig(hiti, tegund):

        if tegund == 'f':
            return reikna_fahrenheit(hiti)
        elif tegund == 'c':
            return reikna_celsius(hiti)
        else:
            return 'Óþekkt hitategund: {}'.format(tegund)

    print(reikna_hitastig(100, 'c'))


Við erum búin að einangra útreikningana í sér föllum sem gerir okkur auðveldara fyrir síðar að endurnota þau. Þetta er meiri kóði en notandinn áttar sig betur á hvað er á seyði.


Hvað gerist ef við prófum að sleppa því að senda tegundina sem færibreytu?

.. code-block:: python


    def reikna_celsius(hiti):
        return hiti * 1.8 + 32

    def reikna_fahrenheit(hiti):
        return (hiti - 32) / 1.8

    def reikna_hitastig(hiti, tegund):

        if tegund == 'f':
            return reikna_fahrenheit(hiti)
        elif tegund == 'c':
            return reikna_celsius(hiti)
        else:
            return 'Óþekkt hitategund: {}'.format(tegund)

    print(reikna_hitastig(100))


    Traceback (most recent call last):
      File "verkefni12.py", line 18, in <module>
        print(reikna_hitastig(100))
    TypeError: reikna_hitastig() missing 1 required positional argument: 'tegund'


Lesum skilaboðin. Fallið *reikna_hitastig()* vantar 1 nauðsynlega færibreytu sem kallast *"tegund"*.


Þegar við skilgreinum færibreytur í föllum getum við gefið þeim sjálfgefið gildi. Hér fyrir neðan fær færibreytan *tegund* gildið *"c"* ef sleppt er að senda hana í fallið. Ef við sendum *"f"* í fallið þá er færibreytan yfirskrifuð.


.. code-block:: python


    def reikna_celsius(hiti=None):
        return hiti * 1.8 + 32

    def reikna_fahrenheit(hiti=None):
        return (hiti - 32) / 1.8

    def reikna_hitastig(hiti=None, tegund='c'):

        if tegund == 'f':
            return reikna_fahrenheit(hiti)
        elif tegund == 'c':
            return reikna_celsius(hiti)
        else:
            return 'Óþekkt hitategund: {}'.format(tegund)

    print(reikna_hitastig(100))


.. _thermo-assignment-12:
    
Verkefni 12
____________

Markmið: Að kalla í eitt fall sem býr til gagnasafn af hitaupplýsingum með endurnýtanlegum kóða.

* Skilgreindu fall sem skilar þér dagsetningunni og tímanum núna.
* Skilgreindu fall sem velur skynjara úr lista með hlutkesti.
* Skilgreindu fall sem býr til slembitölu sem nota má sem hitastig.
* Skilgreindu fall sem skilar þér gagnasafni með 100 stökum af hitaupplýsingum
