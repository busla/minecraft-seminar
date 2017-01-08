.. _thermo-functions:

Föll (functions)
=================

Fall er safn af skipulögðum og endurnýjanlegum kóða sem er notaður til að framkvæma eina eða fleiri aðgerðir.

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



