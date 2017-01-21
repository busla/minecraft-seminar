HTML Tög
========

**Það sem þarf að hafa í huga varðandi HTML tög**

Núna ætlum við að nánar um HTML tög. Tilgangur HTML taga er einfaldlega sá að merkja textann sem ætlum að hafa í vefsíðunni til þess að geta unnið síðan nánar með hann í CSS og JavaScript. Í gamla daga, þegar að CSS var ekki eins stórt mál og það er núna voru vefsíður látnar líta vel út með því að láta HTML tögin sjá um að stýla textann. Þetta er ekki gert lengur, en það er mikilvægt að hafa þetta í huga vegna þess að HTML tög eru ennþá með ákveðna grunnstýla áfasta. Við munum útskýra þetta allt nánar þegar að við lærum meira um CSS. 

**Merking með HTML**

Þegar að við erum að sjá fyrir okkur merkingar með HTML er mjög hjálplegt að ýminda sér hús. Ef að við merkjum hvern einasta hlut í herbergi eftir því hvað þessi hlutur inniheldur, verður það fljótt mjög einfalt að miða á eitthvern einn hlut í húsinu, segjum til dæmis að við viljum miða á eitthvern stól í eldhúsinu. Ef við þekkjum ekkert til hússins byrjum við kannski að skoða það að utan og spurjum okkur, er þetta rétt húsnúmer, býr rétta fólkið hérna? Til þess að fá svar við þessum spurningum er hentugt að virða húsið fyrir okkur að utan, því það veitir okkur allskyns upplýsingar um húsið án þess að þurfa að fara inn í það. Ef allt er í góðu og við erum fyrir utan rétta húsið er tilvalið að ganga bara beint inn. Þegar að við förum fyrst inn í húsið þurfum við að ákveða hvaða hluta hússins við ætlum að ganga að næst, ætlum við á efri eða neðri hæðina, hver hæð fyrir sig er síðan með nokkur herbergi og hvert herbergi er síðan með hver og sín eigin húsgögn. 

Vefsíður virka á sama hátt. Við erum í raun og veru bara með hólf sem innihalda önnur hólf sem innihalda síðan á endanum textan sem við viljum vinna með.

*Dæmi:*

.. code-block:: html

    <!DOCTYPE HTML>
    <html>
        <head>
            <title>Námskröfur</title>
            <meta charset="utf-8" />
        </head>
        <body>
            <h1>Koder.is</h1>
            <ol>
                <li>Nemandi skal ljúka 9 einingum á önn hið minnsta. </li>
                <li>Heimilt er að víkja frá þessu ákvæði ef um er að ræða:</li>
                <ul>
                    <li>Sérstaka erfiðleika í námi, svo sem lesröskun eða fötlun</li>
                    <li>Lokaönn í námi.</li>
                    <li>Nemendur á námssamningi.</li>
                    <li>Nemendur á fyrstu önn í námi.</li>
                </ul>
                <li>Nemandi sem fellur á önn fær aðeins heimild til innritunar á næstu ö...</li>
                <li>Nemandi sem fallið hefur á tveimur önnum í röð eða þrem önnum samta...</li>
                <li> Falli nemandi á önn á hann rétt á að láta þá áfanga standa þ...</li>
            </ol>
        </body>
    </html>

**Lokun HTML taga**

Þið takið kannski eftir því hér fyrir ofan að við lokum ekki öllum HTML tögum. Eitt af þeim sem að við lokum ekki er <meta/> tagið. Það er vegna þess að meta tagið inniheldur ekki neitt efni í sjálfu sér og er þess í stað með svokallað *attribute* sem er í raun og veru bara stillingarartiði fyrir HTML túlkinn. Við förum miklu nánar í nokun	

**Hérna mæli ég með því að þið skoðið HTML kaflan í efni, hann mun hjálpa ykkur við að læra hvenær nota skal hvaða tag**

Verkefni 1
----------

* Setjum upp einfaldan innkaupalista í HTML
* Fiktum í grein á Wikipediu
* Setjum upp lagatexta með innbyggðum stýlum HTML taga
