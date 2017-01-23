Hvað er Javascript?
===================

Javascript er forritunartungumál, það er oftast notað með vefsíðum. Fólk hefur gert allskyns hluti með Javascript meðal annars leiki og veföpp en er oftast notað fyrir flott effects á síðum. Þú notar Javascript til að breyta hlutum á síðum, færa þá, fela þá, stækka þá og helling af öðrum hlutum. Flest allar síður sem eru til nota Javascript, enda er það eitt af vinsælustu forritunartungumálum heimsins.


Ef þú ætlar að skrifa Javascript kóða í HTML skránni þinni þarftu að búa til script tag og skrifar svo kóðan þinn inn í script tagið. Það er líka til mun þæginlegri aðferð, með því að hafa sér skrá fyrir Javascript kóðann og tengja hann svo við síðuna, eins og við gerðum með css. Svo skrifar maður  kóða beint í skránna. Þegar þú býrð til Javascript skrá vistaru hana sem .js skrá.

Svona myndi maður búa til script tagið

.. code-block:: html

	<!DOCTYPE html>
	<html>
		<head>
			<title> Koder </title>
		</head>
		<body>
			<script>
			 //Hérna myndiru skrifa Javascript Kóða
			</script>
		</body>
	</html>

Hérna erum fyrir neðan erum við búnir að tengja html skránna við Javascript skrá, kannski takiði eftir því að maður bendir ekki alveg eins á skrár og í css, þar er notað href en með Javascript notar maður src. Svo seigjum við tegundina á skránni með type, en það er valkostur. Þegar þú ert að nota script tagið til þess að benda á Javascript skrá máttu hafa hana í head eða body, en ekki báðum. Í flestum tilfellum er betra að hafa hana neðst nirði í body því þá hlaðast hún inn síðast sem getur komið í veg fyrir villur ef kóðinn bendir á eitthvað sem er ekki búið að hlaðast.

.. code-block:: html

	<!DOCTYPE html>
	<html>
		<head>
			<title> Koder </title>
		</head>
		<body>
			<script type="text/javascript" src="js/javascript.js"></script>
		</body>
	</html>



**Comment**

Það er mjög góður vani að kommenta kóðan þinn, komment er texti sem þú skrifar en hefur enginn áhrif á kóðan, hann er bara skrifaður til að úskýra hluti og virkni þeirra. Til að búa til Komment skrifaru // Og svo textann sem þú vilt hafa kommentaðan. Ef þú ert að "debugga" einsog það er kallað á ensku, sem er bara að fara yfir kóða og finna villur er mjög gott að commenta kóða út til að kíkja hvort hann valdi villunni.

Dæmi um hvernig Comment virkar

.. code-block:: Javascript

	//Þetta er Komment
	alert("Javascript er geðveikt!");// <- Þarna er kóði, en þetta er Komment

**console.log()**

console.log() er verkfæri sem er innbyggt í Javascript. Það skýrir sig líklega sjálft, en það er notað til að skrifa í consoleið, Til að komast inn í console á vefsíðunni þinnu þarftu að opna hana með einhverjum vafra, hægri klikka á síðuna og velja inspect. Þá koma nokkrir flipar og console er einn af þeim. console.log() verkfærið skrifar það út sem þú setur á milli svigana.

Dæmi um hvernig console.log() skipuninn virkar

.. code-block:: Javascript

	//Til að skilgreina að þú ert að skrifa texta geriru tvöfaldar eða einfaldar gæsalappir
	console.log("Hello world");

.. todo::

	Þarf að sýna á mynd hvernig maður finnur console

**Verkefni 1.** 

Bættu Javascript skrá við síðuna þína. Inni í Javascript skránni þinn notaru console.log() skipunina og átt að skrifa út "Við náðum að tengjast", athuga að þú þarft að nota inspect til að sjá hvað var skrifað í consoleið
