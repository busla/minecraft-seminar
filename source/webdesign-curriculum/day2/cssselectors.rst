CSS Selectors
=============

**Hvað eru CSS selectorar?**

Núna ætlum við að fjalla stutt um það sem kallast *CSS Selectors*. Þegar að við erum að vinna með CSS og ætlum að láta eitthvað HTML *element* líta út á eitthvern sérstakann hátt þurfum við að sjálfsögðu að vita hvernig við eigum eiginlega að tilgreina hvaða HTML tag, eða hvaða týpu af HTML tögum við ætlum að stýla. Þarna koma þessir *CSS selectorar* inn okkur til mikillar aðstoðar.

**Almenn málfræði CSS klasa (Þegar vísað er í "class" eigindið):**

.. code-block:: CSS
    
    .className{
        width:50%;
        border-right:4px solid black;
        padding-right: 17px;
        font-family: Arial;
    }

Það sem við ættum að taka eftir hérna er að þegar að við vísum í "class" eigindið á eitthverju HTML tagi notum við punkt, og skrifum þar á eftir titil eigindisin, sem er í þessu tilfelli einfaldlega *className*. Annað sem er mikilvægt að taka eftir hérna er að við notum slaufusviga til þess að halda síðan utanum stýlana sem við ætlum að setja á klasann sjálfann. Það er síðan innihald þessara slaufusviga sem ráða því hvaða stýla elementið okkar fær. 

**Almenn málfræði CSS klasa (Þegar vísað er í "id" eigindið):**

.. code-block:: CSS
    
    #className{
        width:50%;
        border-right:4px solid black;
        padding-right: 17px;
        font-family: Arial;
    }

Þegar við vísum í "id" eigindið í stað "class" eigindisin virkar þetta alveg eins, nema hvað að við notum myllumerki *(e. hashtag)* og köllum síðan á stýlana sem við viljum að eigum við HTML tagið

**Almenn málfræði CSS klasa (Þegar ekki er vísað í eigindi):**

.. code-block:: CSS
    
    h1{
        width:50%;
        border-right:4px solid black;
        padding-right: 17px;
        font-family: Arial;
    }

Það er einnig hægt að vísa bara í titil HTML tagsins, en ef þetta er gert munu stýlarnir eiga við öll tög af þessari gerð

**Nánar um eigindalausa CSS selectora**

Þegar að við erum að vísa í eitthvað *element* án þess að tilgreina eitthvern "class" eða "ID" þá erum við að vísa í *elementið* án þess að nota eigindin. Þetta er mjög gagnlegt, en getur líka verið töluvert flókið.

Gefum okkur þetta HTML tré: 

.. code-block:: HTML

    <header>
        <div class="headerLogo"></div>
        <nav>
            <ul class="navContainer">
                <li class="navItem"><a href="#about">Leiðin</a></li>
                <li class="navItem"><a href="#organization">Búðirnar</a></li>
                <li class="navItem"><a href="#qualifications">Inntökuskylirði</a></li>
                <li class="navItem"><a href="#hr">Samstarf við HR</a></li>
                <li class="contactLink navItem"><a href="#contact">Hafa samband</a></li>
            </ul>
        </nav>
    </header>

Ef við myndum þá vilja láta textan inni í linkunum inni í listanum vera *skáletraða* höfum við nokkrar aðferðir til þess að gera það.

Sú fyrsta væri að kalla einfaldlega í klasann og setja stýlinn á það. Þessi aðferð myndi líta svona út:

.. code-block:: CSS

    .navItem{
        font-style: italic;
    }

Önnur leiðin væri að sjálfsöðu að stýla bara öll <li> tög á þennan hátt.

.. code-block:: CSS

    li{
        font-style: italic;
    }

Vandamálið við þessa aðferð er samt að þá verða öll <li> tög á síðunni okkar *skáletruð* og það er ólíklega það sem við viljum. 

Ef við viljum eingöngu miða á <li> tög sem eru inni í navigation-menu, myndum við gera það svona.

.. code-block:: CSS

    header nav ul li{
        font-style: italic;
    }

Núna erum við í raun og veru að segja "allur texti inni í <li> tögum sem eru inni í <ul> tögum sem eru inni í <nav> tögum sem eru inni í <header> tögum eiga að vera *skáletruð*"

.. todo::

    Bæta inn í þetta link þar sem að við tölum um nested HTML tög og hvernig það virkar. 


