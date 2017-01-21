Föll, hlutir og listar
======================

Föll
____

Föll eða functions á ensku líka kallað aðferðir, Console.log() er innbyggt fall í Javascript, það eru til helling af innbyggðum Javascript föllum sem við getum notað. Það er eitt að nota fall en það er annað að búa það til sem við ætlum að gera í þessum kafla.

*Dæmi um fall*

.. code-block:: Javascript
	
	var ta1 = 5;
	var ta2 = 10;

	//fallið
	function times(tala1,tala2) {
		return tala1 * tala2;
	}
	var sum = times(ta1,ta2);

Hérna fyrir ofan erum við með mjög einfalt fall, til að skilgreina að þú sért að búa til fall skrifaru function, svo kemur nafnið á fallinu sem í dæminu fyrir ofan myndi vera times. Svo geriru sviga, og inni í svigunum eru hlutir sem fallið tekur við. Semsagt ef þú kallar í þetta fall, vill fallið fá 2 hluti sem hún mun nota inni í fallinu. Við seigjum að breytann sum sé jafnt og fallið times með tveim breytum. Þá kölluð við á fallið með þessum tveim breytum sem return mun svo skila margfeldi þeirra. 

.. todo::
	
	Betri útskýringar á föllum og hvernig þær hegða sér.

*Fall sem reiknar ummál kassa*

.. code-block:: Javascript

	var lengd = 5;
	var breidd = 10;

	function Reiknaummal(b,l) {
		return b + b + l + l;
	}
	var ummal = Reiknaummal(breidd,lengd);

Þetta fall tekur inn tvær tölur, ein sem myndi vera breidd og önnur sem myndi vera lengd. Svo reiknar út ummálið af kassa með tölunum og skilar niðurstöðunni.

*Fall sem finnur út hvaða tala er hæst*

.. code-block:: Javascript

	var tala1 = 10;
	var tala2 = 20;
	function Staerri(t1,t2) {
		if(t1 > t2) {
			return "Tala eitt er stærri en tala tvö";
		}
		else if(t1 < t2) {
			return "Tala tvö er stærri en tala eitt";
		}
		else {
			return "Þær eru jafn stórar";
		}
	}
	console.log(Staerri(tala1,tala2))

Þetta fall tekur inn tvær tölur og finnur út hvor þeirra er stærri. Fallið skilar svo streng þannig hægt sé að kalla þetta í console.log fallinu.

**Verkefni 1**

Búiði til fall sem margfaldar tölu með 20

**Verkefni 2**

Búiði til fall sem tekur inn tvær tölur, og skrifar svo út allar tölur sem eru á milli þessara talna.

**Verkefni 3**

Búiði til fall sem sameinar tvo strengi.

Hlutir
______


Í Javascript geturu búið til hluti eða Objects á ensku. Flestir hlutir sem þú myndir búa til hafa einhverja eiginleika og hluti sem þeir geta gert.

*Dæmi um hlut/Object*

.. code-block:: Javascript

	var persona = {
		fyrstanafn : "Henry",
		eftirnafn : "Joe",
		aldur : 50,
		haed : 180
	}

Hérna erum við með hlut sem heitir person og geymir fjórar breytur. Hver breyta sem hann geymir hefur sitt eigið nafn þannig þetta er einsog breyta sem hefur fjórar aðrar breytur inni í sér. Eftir hvern eiginleika sem þú býrð til seturu kommu eftir hann ef þú ætlar að hafa fleirri eiginleika. Þannig síðasti eiginleikinn myndi ekki hafa kommu.

*Kalla á eigindi eða breyta eigindi*

.. code-block:: Javascript
	
	//Myndi skrifa út fyrstanafn sem væri Henry
	console.log(persona.fyrstanafn);
	//breytir fyrstanafn í Jóhannes
	persona.fyrstanafn = "Jóhannes";

*Hlutir geta líka geymt í sér föll, einsog ef við myndum búa til hlut sem væri maður, gæti hann verið með fall sem myndi seigja nafnið hans.*

.. code-block:: Javascript

	var persona = {
		fyrstanafn : "Birkir",
		eftirnafn : "Gunni",
		aldur : 15,
		haed : 190,
		segjanafn : function() {
			return this.fyrstanafn + " " + this.eftirnafn;
		}
	}
	console.log(persona.seigjanafn());

Hérna bættum við fallinu segjanafn við hlutinn persona, ef við ætlum að nota eitthvað af eigindum sem voru skilgreind fyrir framan þurfum við að nota this.fyrstanafn, þá er this að benda á hlutinn sem við erum inni í sem myndi vera persona, og þá væri this.fyrstanafn bara einfaldlega persona.fyrstanafn.

**Verkefni 1**

Búiði til hlut/object sem er bíl, hann þarf að hafa eigindin tegund, bílnúmer, fjöldi farþega og litur. Skrifiði svo út öll eigindin í consoleinu.

**Verkefni 2**

Búiði til hlut/object sem er dýr, það þarf að hafa eigindin nafn, tegund, þyngd og fjöldi fóta. Hluturinn þarf að hafa fall sem seigir allar upplýsingar um sjálfan sig.

Listar
______

Listar eða á ensku Arrays eru breytur sem hafa þann kost að geta geymt margar breytur inni í sér. Þær eru mjög hentugar til að geyma fljölda upplýsingar í einni breytu. Listar hafa líka þann valmöguleika á að geyma marga lista sem geyma hver og einn margar breytur, en þá er þetta orðið dálítið flókið. Listar eru búnir til einsog aðrar breytur en þeir geyma fylki af tölum sem þú skilgreinir með hornsvigum. Svo greiniru milli hvers staks með kommu. Hvert stak í lista hefur sína stöðu í röðinni sem er kallað index á ensku. Maður notar það til á einhverja sérstaka tölu í listanum. Fyrsta talan hefur indexið 0, og svo næsta 1 og svo koll af kolli.

*Hvernig listi sem inniheldur bara tölur virkar*

.. code-block:: Javascript

	//Index talna  0 1 2 3 4 5 6 7  8  9  10   11      
	var listi  =  [1,5,6,7,8,9,0,10,14,44,543,3333];
	//Með þessum indexum getum við callað í tölurnar
	console.log(listi[4]); //Hvað myndi þetta birta?

Kóðinn fyrir ofan er mjög einfalt dæmi um hvernig listar virkja. Listar eru mjög nothæfir, í næsta dæmi ætlum við að skoða hvernig við getum skoðað öll stök í einhverjum lista, með hjálp for lykkjunnar sem við lærðum.

*Skoða öll stök í lista*

.. code-block:: Javascript

	//Listinn
	var listi = [20,55,10,15,80,90];
	for (var a = 0; a < listi.length; a++) {
		console.log(listi[a]);
	}

Það sem þessi kóði gerir er að skrifa út öll stökin í listanum, en hvernig fer hann að því? Hann byrjar á að skrifa for lykkju sem keyrir frá 0 og þangað til lengdin á listanum er ekki stærri en a, þannig þetta keyrir jafn oft og lengd listarins og byrjar á 0. Þá getum við einfaldlega skrifað út eftir hverja keyrslu stakið í lista sem lykkjan er á. .length er innbyggt verkfæri í javascript sem verður farið betur í kaflanum "Innbyggð verkfæri".

*Summa allra staka í lista*

.. code-block:: Javascript
	
	var listi = [1,2,3,4,5,6,7,8,9,10];
	var sum = 0;
	for (var a = 0; a < listi.length; a++) {
		sum += listi[a];
	}
	console.log(sum);

Þessi kóði gerir nákvamlega sama og fyrri kóðinn, fyrir utan að hann plúsar öll stökinn við breytuna summa og skilar svo út gildi summu þegar for lykkjan er búin að keyrast.

*Listi af strengjum*

.. code-block:: Javascript

	//Index strengja  0        1       2            3          4
	var listi = ["Javascript","er","geðveikt","skemmtilegt","tungumál"];
	for (var a = 0; a < listi.length; a++) {
		console.log(listi[a]);
	}

Seigjum að við séum með lista sem inniheldur ekki neinu, og við ætluðum að bæta við hann öllum sléttum tölum frá 1-100. Þá getum við notað mjög þæginlega aðferð sem heitir push. Þá mun ýta einhverju gildi inn í listan sem við veljum.

*Listi af sléttum tölum*

.. code-block:: Javascript

	//skilgreinum tómann lista
	var slettar = [];
	for (var a = 1; a <= 100; a++) {
		if (a % 2 == 0) {
			slettar.push(a);
		}
	}
	console.log(slettar);

Við byrjum á að skilgreina tómann lista sem heitir slettar. Svo keyrum við for lykkju frá 1 upp í 100, ef breytan a sem fer hækkandi um einn eftir hverja keyrslu er deilanleg með tveimur og gefur engann afgang þá setjum við hana í listann. Þá geriru nafnið á listanum sem eru slettar svo .push sem er innbyggð aðferð í javascript, svo inni í svigunum hvað þú vilt setja í arrayinn, sem væri í þessu tilfelli breytan a ef hún er deilanleg með tveimur. Svo skrifum við út slettar sem mun bara skila öllum listanum.


**Verkefni 1**

Búiði til lista sem geymir einhverjar tölur af ykkar vali, skrifið svo út allar þessar tölur með for lykkju.

**Verkefni 2**

Búiði til lista með tölunum 1-10, skrifið listann út í öfugri röð með for lykkju.

**Verkefni 3**

Skrifiði for lykkju sem setur allar tölur frá 0-1000 í lista, finnið svo summu allra gilda í listanum.