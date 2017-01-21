CSS Pseudo-selectors
====================

CSS Pseudo-selectors eru mjög nátengdir CSS selectorunum sem við vorum að ljúka við að tala um, nema hvað að þeir eiga við þegar að við viljum hafa áhrif á stýl eitthvers *elements* undir eitthverjum sérstökum kringumstæðum, til dæmis ef mús notendans svífur yfir *elementinu*

Það eru til margir pseudo-selectors sem við notum við hinar og þessar aðstæður, en þeir sem við munum fara yfir eru aðallega *:hover* og *:visited*. En um leið og þið skiljið nokkurnvegin hvernig pseudo-selectors virka þá skiptir það ekki máli hvern þeirra þið eruð að nota, því að málfræðin er undir öllum kringumstæðum eins. 

Hérna er dæmi um hvernig pseudo-selector er notaður til þess að breyta lit *<a>* tagsins þegar að bendillinn svífur yfir það:

.. code-block:: CSS

    a:hover{
        color: orange;
    }

Annað dæmi, hérna notum við *:visited* til þess að breyta lit hlekkja sem notandinn er búinn að ýta á:

.. code-block:: CSS

    a:visited{
        color: purple;
    }

