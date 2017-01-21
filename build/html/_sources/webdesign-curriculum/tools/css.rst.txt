CSS
===

Hérna er allt helst um css sem þú munt nota í námskeiðinu.

Tenging
_______


Til þess að bæta CSS skrá við HTML skránna þína er þetta ein mjög einföld lína, sem þú bætir við í headerinn

.. code-block:: html

	<head>
		<link rel="stylesheet" type="text/css" href="css/main.css">
	</head>

Þetta skiftist niður í þrjá parta, þú getur sleppt rel og type, en verður alltaf að hafa href til að seigja staðsetningu skránnar.

**rel** sem skilgreinir tenginguna á milli, sem við setjum inní stylesheet sem þíðir stílsíða.

**type** sem tekur inn tegund skráarinnar, text því þetta er textaskrá og css fyrir tungumálið.

**href** tekur inn staðsetningu skráarinnar.

Stílar
______

Stílar er það sem þú notar mest af í css, þú skrifar hvaða stíl þú vilt breyta og svo í hvað.

**Dæmi :**

.. code-block:: css

	color: blue;

Color er þá hluturinn sem þú vilt breyta, og svo í hvað sem er blue

**Upplýsingar um marga stíla og hvernig þú notar þá**

.. todo::
    
    Þarf að finna út hvernig ég collapsa neðangreindu stíla

*color*

*background-color*

*font-family*

*font-size*

*font-style*

*font-weight*

*letter-spacing*

*width*

*height*

*margin*

*padding*

*border*

*float*

Meira um þetta getur fundið hér  `W3Schools Styles`_.

Tög
___

Þú getur líka breytt stíl á tögum, þá myndi alltaf þegar þú myndir búa til tagið myndi það sækja í stílana.
Til að breyta stílum taga skrifaru nafnið á taginu, opnar sviga, skrifar hvaða stíla þú vilt nota og lokar sviga.

**Dæmi 1**

.. code-block:: css

	h1 {
		color: blue;
		font-size: 20px;
		letter-spacing: 2px;
	}

Þetta myndi breyta öllum h1 tögum, þau myndu fá bláan lit, leturstærð 20 pixla, og 2px á milli hvers stafs.

**Dæmi 2**

.. code-block:: css

	div {
		width: 200px;
		height: 200px;
		padding: 50px;
	}

Þetta myndi breyta öllum div tögum, gef þeim hæð og breydd 200px, svo myndi það bæta við padding, sem býr til pláss frá endum myndarinnar til að textar eða myndir inní tögunum séu ekki alveg úti á enda. Svo divið sjálft myndi vera 300px á hæð og breydd, því 50 pixlar myndu bætast á top, botn, hægri, og vinstri hlið kassans.

Klassar
_______

Klassar er samanblanda af mörgum stílum, þú munt alltaf nota Klassa, heldur enn að skrifa einn stíl. Til að búa til klassa geriru punk "." og svo nafnið á klassanum opnar svo sviga, skrifar stílana inní og lokar.

**Dæmi 1**

.. code-block:: css

	.textastill {
		color: blue;
		font-size: 30px;
		text-align: center;
	}

Þetta myndi breyta lit í bláan, stærð leturs í 30px og hafa textan í miðjunni

**Dæmi 2**

.. code-block:: css

	.header {
		width: 100%;
		height: 50px;
		background-color: red;
		border: 2px solid black;
	}

Klassinn header, væri fyrir hausinn á síðunni þinni, hann myndi vera með breydd 100% sem væri þá allur skjárinn þinn, hæð væri 50 pixlar, bakgrunnslitur væri rauður. Svo kemur aðeins flóknari stíll sem heitir **border**. Hann tekur inn stærð, tegund og lit, þetta býr til ramma í kringum tagið sem er 2 pixlar á breidd, línan er heil og væri svört á litinn.

Meira um klassa er að finna hér `W3Schools Class`_.

Pseudo Selectors
________________

Pseudo selectors, eru notaðir til að skilgreina sérstaka stöðu einhvers tags, skjéllum okkur bara beint í dæmi.

**Dæmi :**

.. code-block:: css

	.textastill:hover {
		color: red;
	}

Þessi stíll myndi aðeins fara í gang þegar það er farið með músina yfir tagið sem inniheldur þessum stíl. Og þá myndi color breytast í rauðan, hinnsvegar ef þú ferð með músina af taginu myndi stílinn ekki vera virkur og breytast í það sem hann var, þá myndi litur verða aftur blár.

**hover** er einn af mest notuðu Pseudo selectorunum, til að nota Peusdo selector þarftu einfaldlega að gera tvípunkt ":" eftir stílnum, skrifa svo nafnið á Pseudo selectorinum sem þú ætlar að nota, opna sviga, skrifa stílana sem eiga að virkjast þegar tagið fer í ástandið, loka svo sviganum.

**Upplýsingar um marga Pseudo Selectors og hvernig þú notar þá**

*:hover*

*:visited*

*:link*

*:first-child*

*:focus*

*:empty*

Meira um Pseudo Selectors er að finna hérna `W3Schools Pseudo`_.

.. todo::
    
    Sama og þarf að gera við hinn

.. _W3Schools Pseudo: http://www.w3schools.com/css/css_pseudo_classes.asp
.. _W3Schools Styles: http://www.w3schools.com/html/html_css.asp
.. _W3Schools Class: http://www.w3schools.com/css/css_syntax.asp