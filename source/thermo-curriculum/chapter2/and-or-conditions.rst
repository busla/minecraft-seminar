.. _thermo-and-or:

Ef að og eða
============

Reglulega notum við fleiri skilyrðingar með *if* og *else*. 

Búið til nýja skrá sem heiti *verkefni6.py* og setjið inn eftirfarandi kóða.

*Dæmi*

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

    if xd + xb >= 32 and xv + xa + xp + xs + xc >= 32: # breyta and í or
        print('Annað hvort Panamastjórnin eða Lækjarbrekkubandalagið')

    else:
        print('Það getur bara hvað sem er gerst!')



.. _thermo-assignment-6:

Verkefni 6
----------
* Sama uppsetning og í *verkefni 5* en nú bætirðu við öðrum 5 breytum og notar *random.randint()* aðgerðina til að skilgreina vindhraða.
* Notaðu and/or til að uppfylla eftirfarandi skilyrði.
  * Allt er helfrosið og ekki úti standandi fyrir vindi
  * Allt er helfrosið og frekar hvasst
  * Allt er helfrosið og blankalogn
  * Steikjandi hiti en menn standa ekki í lappirnar fyrir vindi
  * Peysuveður og hviður inn á milli
  * Skítkalt en blankalogn


