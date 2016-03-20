.. _verkefni14:

Verkefni 14
===========

Í þessu verkefni ætlum við að skoða lykkjur betur. Lykkja er aðgerð sem endurtekur sig á meðan eitthvað er satt.

Sem dæmi þá gætum við athugað hvort 1 sé jafnt og 1. Er það ekki örugglega satt?

Á meðan það er satt þá viljum við gera eitthvað skemmtilegt eins og skrifa út nafnið okkar.

Athugaði að forritið þitt mun skrifa nafnið þitt endalaust því að 1 verður alltaf 1.

*Dæmi*

.. code-block:: python

    á meðan 1 == 1:
        skrifa *Jón*


Við getum prófað þetta í Python. Við skulum nota *True* sem þýðir *satt* á íslensku. Á meðan *satt* prentaðu út hvað klukkan er *núna*.

.. code-block:: python
    
    import time

    while True == True:
        print(datetime.now())
        time.sleep(1)

Það má líka bara skrifa *True*

.. code-block:: python
    
    import time

    while True:
        print(datetime.now())
        time.sleep(1)


Prófaðu að láta forritið gera eitthvað annað en að skrifa hvað klukkan er.

