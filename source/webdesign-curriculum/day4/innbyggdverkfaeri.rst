Innbyggð Verkfæri og DOM
========================

DOM Sækja gögn
______________

DOM stendur fyrir Document Object Modeling. Í stuttum samandrætti er DOM það sem þú notar í Javascript til sækja gögn frá síðunni þinni til að breya þeim, eða bæta við gögnum á síðuna þína og margt fleirra. Í fyrstu munum við fara yfir hvernig við sækjum gögn. Gefum okkur það að html kóðinn okkar hérna fyrir neðan er síðan okkar. Við ætlum að breyta textanum sem er í h1 taginu, við bætum við id á hann sem heitir header og það gerir okkur kleyft að finna hann mjög auðveldlega í javascript.

*HTML*

.. code-block:: html

    <!DOCTYPE HTML>
    <html>
        <head>
            <title>Námskröfur</title>
            <meta charset="utf-8" />
        </head>
        <body>
            <h1 id="header"> Koder.is </h1>
        </body>
        <script type="text/javascript" src="js/main.js"></script>
    </html>

*Javascript*

.. code-block:: Javascript

	//geymum upplýsingar um tagið í breytunni tag
	var tag = document.getElementById("header");
	tag.innerHTML = "Koder.com";

Þið ættuð öll að þekkja hvernig html skjalið virkar, en nú eru komnir eitthvað nýtt í Javascript skjalið. Það fyrsta sem þið takið eftir er document.getElementById() alltaf þegar þú ætlar að nota eitthverja DOM skipun verður fyrst að kalla í document. Svo komum við að skipuninni getElementById sem sækjir tag sem hefur idið sem þú setur á milli svigana. Þá myndi þessi kóði sækja tagið h1 sem hefur ideið header. Þá erum við að geyma upplýsingar um tagið h1 í breytunni tag, þá getum við byrjað að vinna með tagið, ef við gerum tag.innerHTML = eitthver texti þá getum við breytt textanum sem er geymdur inni í taginu. Hann myndi þá breytast frá "Koder.is" í "Koder.com".

Næsta aðferð sem við ætlum að nota til að sækja gögn er document.getElementsByTagName sem sækjir upplýsingar um öll tög af einhverju tagi. Þetta myndi skila sér til baka sem lista þannig við gætum unnið með mörg gögn í einu. Sem er mjög hentugt til að breyta classa eða texta af eitthverjum sérstökum tögum.

*HTML*

.. code-block:: html

    <!DOCTYPE HTML>
    <html>
        <head>
            <title>Námskröfur</title>
            <meta charset="utf-8" />
        </head>
        <body>
       	    <ul>
       	        <li>Texti 1</li>
       	        <li>Texti 2</li>
       	        <li>Texti 3</li>
       	        <li>Texti 4</li>
       	    </ul>
        </body>
        <script type="text/javascript" src="js/main.js"></script>
    </html>

*Javascript*

.. code-block:: Javascript

	// Breytan tog geymir upplýsingar um öll li töginn
	var tog = document.getElementsByTagName("li");
	for (var a = 0; a < tog.length; a++) {
		tog[a].innerHTML = "Breyttum öllum textanum";
	}

Fyrst í Javascript kóðanum sækjum við öll tög af tegundunni li, með skipununni getElementsByTagName. Það sækjir öll tög og skilar þeim sem lista, sama þótt það sé bara eitt tag. Svo keyrist for loopa sem fer í gegnum öll stök í listanum og breytir textanum þeirra með innerHTML. Takið eftir því að maður þarf fyrst að finna stakið með tog[] og í svigunum númerið á stakinu. 

Síðasta skipunin í DOM sem við ætlum að nota til að sækja gögn er document.getElementsByClassName, það sækjir öll tög sem hafa einhvern css klassa fastan við sig. Það mun líka skila gögnunum sem lista og þörfum við að meðhöndla þau þannig. Þetta virka mjög líkt og getElementsByTagName fyrir utan að það sækjir eftir klössum.

*HTML*

.. code-block:: HTML

    <!DOCTYPE HTML>
    <html>
        <head>
            <title>Námskröfur</title>
            <meta charset="utf-8" />
        </head>
        <body>
       	    <div class="main"> Halló Heimur </div>
       	    <div class="main"> Halló Heimur </div>
       	    <div class="main"> Halló Heimur </div>
       	    <div class="main"> Halló Heimur </div>
       	</body>
        <script type="text/javascript" src="js/main.js"></script>
    </html>

*Javascript*

.. code-block:: Javascript

	var tog = document.getElementsByClassName("main");
	for(var a = 0; a < tog.length; a++) {
		tog[a].innerHTML = "Box númer " + (a+1);
	}

Javascript kóðin fyrir ofan sækjir öll tög sem eru með klassan main og geymir þau í lista í breytunni tog. Svo keyrist for lykkja sem fer frá null og í lengdina á listanum tog. Í hvert skifti sem hún keyrir breytir hún einum af stökunum í listanum tog, og breytir textanum í stakinu í "Box númer " og númerið á for lykkjunni.

DOM Breyta gögnum
_________________

**innerHTML**

Í öllum sýni dæmunum fyrir ofan erum við alltaf að nota innerHTML, en hvað gerir það? Það sækjir textan sem er inni í taginu, svo getur þú unnið úr upplýsingunum eða jafnvel breytt þeim. innerHTML er eiginleiki.

*innerHTML Dæmi*

.. code-block:: Javascript

  //Sækjum tagið
  var tog = document.getElementById("header");

  //Skrifum út textan sem er inni í taginu
  console.log(tog.innerHTML);

  //Breytum textanum inni í taginu
  tog.innerHTML = "Breyttur texti":

**className**

className er eiginleiki sem er hægt að kalla á til að sækja upplýsingar um klassana sem eru tengdir við tagið, og líka til að breyta þeim. Þá geturu skoðað hvort eitthvað tag hefur klassa, þú getur breytt klassa eða jafnvel bætt klassa við annan klassa.

*className*

.. code-block:: Javascript

  //sækjum tagið
  var tog = document.getElementById("header");

  //skrifar út klassa sem eru tengdir taginu
  console.log(tog.className);

  //Bætir klassanum flott við tagið
  tag.className += "flott";

  //Segir að klassarnir séu bara þeir sem eru á milli gæsalappanna
  tag.className = "h1 d22 gulur";


**id**

id er eiginleiki sem hægt er að kalla á til að sækja upplýsingar um idið sem tagið er með og líka breyta því.

*id*

.. code-block:: Javascript
  
  //Sækjir tagið
  var tag = document.getElementById("header");

  //skrifar út idið sem tagið header breytan tag er með
  console.log(tag.id);

  //breytir idinu í rkv
  tag.id = "rkv";

  //Takið eftir ef þessi kóði myndi keyra aftur myndi hann ekki virka,
  //því þá myndi hann sækja í header id og ekkert myndi skilast

**addEventListener**

addEventListener er eiginleiki sem þú getur bætt við tagið þitt, það bætir við event listener, sem hlustar á eitthvað gerast. Því þetta getur orðið smá flókið ætlum við bara að læra á einn hlut sem það getur hlustað eftir. Það er Click, semsagt þetta mun bíða og hlusta þangað til eitthver klikkar á tagið ef svo gerist keyrir hann fall sem er innan í.

*addEventListener*

.. code-block:: Javascript
    
  //Sækjir tagið
  var tag = document.getElementById("header");

  //bætir addEventListener á tagið
  tag.addEventListener("click", function() {
    console.log(this.innerHTML);
    console.log(this.id);
  });

Núna í hvert skifti sem það er klikkað á tagið mun það skrifa út tvær línur. Það mun skrifa this.innerHTML þá er this að benda á hlutinn sem var klikkað á sem er tagið. Þá mun það skrifa út textan sem er í taginu, og idið sem tagið er með.

.. todo:: 

  Bæta við mun fleirri DOM properties
  Veit ekki alveg hver ég á að velja

DOM búa til tög
_______________

Í Javascript þarftu ekki alltaf að sækja tilbúin tög, heldur getur þú búið til þín eigin tög. Eftir að þú býrð til þitt eigið tag mun það ekki hafa neitt þannig þú þarft að gefa því klassa, texta og allt sem það þarf til að virka. Það er kóði sem mun allur skrifast í Javascript. Eftir að þú ert búin að láta tagið fá allt sem það þarf, þurfum við að setja það á síðuna, Þá finnum við tagið sem það á að vera í og setjum það inn í tagið. Hérna fyrir neðan verða betri útskýringar um hvernig við bætum því við

*Búa til tög dæmi*

.. code-block:: Javascript
  
  //Býr til tagið div
  var tag = document.createElement("div");

  //Bæti við klassa og texta
  tag.innerHTML = "Þetta er div";
  tag.className = "div3";

  //Ná í tag sem er með id body
  var body = document.getElementById("body");

  //Setjum tagið inn í body tagið
  body.appendChild(tag);

Fyrsta sem við gerum er að búa til breytu tag sem geymir gildin af nýju tagi af tegundinni div. Skipunin document.createElement() býr til nýtt tag af tegundinni sem þú setur inn í svigana. Eftir að við búum til tagið bætum við texta og klassa í það. Svo sækjum við annað tag sem er með "body" id. Svo notum við appendChild skipunina sem öll tög hafa. Semsagt ef þú vilt setja eitthvað tag inn í vefsíðuna verður hún að vera á milli einhverja stærra taga. Svo þú finnur tagið sem þú vilt að haldi utanum þitt tag og bætir við taginu sem child þar inn.

.. todo:: 

  Ruglandi útskýringar, þarf betra