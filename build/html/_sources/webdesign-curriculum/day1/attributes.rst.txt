Eigindi
=======

Eigindi *(e. Attributes)* eru auka stillingar sem við getum sett inn í HTML tög. Þessar stillingar geta meðal annars sagt okkur hvaða stýlar eiga að vera tengdir við tagið, hvaða einkenni það á að hafa eða jafnvel hvaðan eitthver skrá á að koma ef við erum að kalla í eitthverja mynd eða skriptu sem við erum með geymda eitthverstaðar annarstaðar í verkefninu okkar. Við munum fara yfir öll helstu eigindi mikilvægustu HTML tagana í þessum kafla en ég hvet ykkur samt sterklega til þess að fara á internetið þegar að þið komið heim og skoða eigindi nánar á vef `Mozilla`_.

Það eru nokkur eigindi sem virka með öllum HTML tögum, en það eru alls ekki öll. Lang flest eigindi virka aðeins með nokkrum tilteknum HTML tögum. Þetta er mjög mikilvægt að hafa í huga og ef þið lendið eitthverntíman í vandræðum með þetta utan námskeiðisins mæli ég með því að þið leitið ykkur einfaldlega svara á netinu.


Hérna er annars stuttur listi af eigindunum sem við munum nota í dag.

.. todo::
    Líklega hægt að finna betri leið til þess að sýna þetta

+------------+--------------------------------------------------+-----------+ 
| Eigindi    | HTML tög                                         | Lýsing    | 
+============+==================================================+===========+ 
| id         | Virkar með öllum tögum                           |           | 
+------------+--------------------------------------------------+-----------+ 
| class      | Virkar með öllum tögum                           |           | 
+------------+--------------------------------------------------+-----------+ 
| href       | Aðallega með <a>                                 |           | 
+------------+--------------------------------------------------+-----------+ 
| src        | <audio>, <embed>, <iframe>, <img>,               |           |
|            | <input>, <script>, <source>, <track>, <video>    |           | 
+------------+--------------------------------------------------+-----------+
| heigth     |                                                  |           | 
+------------+--------------------------------------------------+-----------+
| width      |                                                  |           | 
+------------+--------------------------------------------------+-----------+

Dæmi um notkun eiginda:
----------------------------------------------------------


**ID eigindið**

Það sem gerir ID eigindið sérstakt er að í hverju HTML skjali má hvert ID bara koma fyrir einu sinni. Þetta er vegna þess að þegar maður notar ID er það vegna þess að maður vill einkenna HTML tagið á eitthvern hátt. Mjög heilbrigt er að hugsa um HTML tög sem kennitölu tagsins. ID eigindið virkar með öllum HTML tögum. 

.. code-block:: html
	
    <div id="nowThisDivHasAnId">

Hægt er að hafa mörg ID á einu HTML tagi, það er sjaldan gert, en þegar maður vill það er einfaldlega notað bil til að aðskilja hvert ID fyrir sig. Með þessu fylgir þá að þegar maður býr til stakt ID má það ekki innihalda bil.

.. code-block:: html
	
    <div id="nowThisDivHasAnId thisDivHasASecondId">

**Class eigindið**

Class eigindið virkar með öllum HTML tögum, alveg eins og ID eigindið en notkun þess aðgreinist frá ID með því að maður er hvattur til þess að nota hvern klasa oft í hverju skjali. 

.. code-block:: html
	
    <div class="nowThisDivHasAClass">

Rétt eins og með ID er líka hægt að hafa marga klasa á einu HTML tagi. Það er gert svona:

.. code-block:: html
	
    <div class="classNumberOne classNumberTwo">

**Href eigindið**

Þegar að maður vill tengja við eitthvað annað skjal en maður er í, notast maður við *href* eigindið. Það er lang algengast að nota href með *<a>* taginu, en hægt er að nota *href* með nokkrum öðrum tögum.

.. code-block:: html
	
    <a href="hérna_sendir_þú_notendann_eitthvert_annað">Þetta er titill hlekksins</a>

Ekki er hægt að hafa mörg gildi inni í href, en hvernig ætti <a> annars að vita hvert það ætti að senda notendann?

**Src eigindið**

Src er notað til þess að láta HTML skjalið vita að við erum að ná í eitthver gögn annarstaðar frá en við erum núna. Src er einfaldlega stytting á source. Þetta virkar í raun og veru nokkurnvegin eind og *href* nema hvað að notandinn þarf ekki að gera neitt til þess að skjalið sé sótt.

.. code-block:: html

    <script src="myscripts.js"></script>

.. todo::
    Bæta við efni um width og height
    
.. _`Mozilla`: https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes

Verkefni 1
----------

* Búðu til lista af hlekkjum, opna vefsíðurnar í nýjum glugga
* Setjum inn eitthverja mynd í ákveðnum stærðum
