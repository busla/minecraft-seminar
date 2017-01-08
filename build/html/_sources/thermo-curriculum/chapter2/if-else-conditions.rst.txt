.. _thermo-if-else:

Hvað ef?
========

Færum okkur úr Python skelinni og opnum IDLE (python 3).

Búið til nýja skrá sem heitir *verkefni5.py* og vistið hana.

.. code-block:: python
        
    xa = 4 # Björt framtíð
    xb = 8 # Framsókn
    xc = 7 # Viðreisn
    xd = 21 # Sjallar
    xe = 0 # Íslenska þjóðf.
    xf = 0 # Flokkur fólksins
    xh = 0 # Húmanistaflokkurinn
    xp = 10 # Píratar
    xr = 0 # Alýðufylkingin
    xs = 3 # Samfylkingin
    xt = 0 # Dögun
    xv = 10 # VG

    if xd >= 32:
        print('Hrein ríkisstjórn sjálfstæðisflokks')

    elif (xd + xb) >= 32:
        print('Ríkisstjórnin heldur velli')

    elif (xd + xb) < 32:
        print('Ríkisstjórnin er fallinn')

    elif (xs + xv + xv) >= 32:
        print('Hrein vinstri stjórn')

    elif (xd + xa + xc) >= 32:
        print('Samtök atvinnulífsins komin á þing með aðeins {} þingmanna meirihluta'.format((63 - xd - xa -xc)))

    elif (xd + xa + xc) < 32:
        print('Samtök atvinnulífsins eru í stjórnaraðstöðu')

    else:
        print('Það getur bara hvað sem er gerst!')

.. _thermo-assignment-5:

Verkefni 5
----------

* Notaðu *import* til að sækja módúluna *random*
* Skilgreindu fimm breytur og notaðu aðgerðina *uniform* sem kemur með *random* módúlunni til búa til slembitölu á bilinu -50 til 50 í hverja breytu.
* Notaðu *if*, *elif* og *else* til að silgreina hitasvið og prenta út lýsingu eftir því sem við á.