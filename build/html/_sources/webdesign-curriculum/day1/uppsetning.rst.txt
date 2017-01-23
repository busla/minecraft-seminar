Uppsetning Vefsíðu
==================

**Hvernig byrjum við eiginlega?**

Til þess að geta byrjað að hanna vefsíður þurfum við fátt annað en vafra og notepad. Það eru samt til tól sem einfalda vinnuna töluvert, þar á meðal er `Sublime Text`_ með þeim bestu, en `Sublime Text`_ er ritvinnsluforrit sem er gætt þeim einstaklegu hæfileikum að gera vefforritun margfalt einfaldari. Það sem `Sublime Text`_ gerir sem einfaldar vinnuna svona mikið er meðal annars að lita ákveðin lykilorð á eitthvern sérstakann hátt, ásamt því að hann notar autocomplete til þess að láta okkur þurfa að skrifa mun minna en við þyrftum annars. 

Fyrir utan að setja upp `Sublime Text`_ þurfum við einungis vafra *( `Firefox`_ , `Chrome`_ , o.s.frv.)*	og þá getum við hafist handa. 

**Beinagrind allra vefa**

Allir vefir eiga það sameiginlegt að vera með sömu grunn-uppsetinguna, hvort sem það er Facebook, Google, eða vefsíðurnar sem að þið eruð að fara að setja saman í dag.

Auk þess að vera með haus og líkama, eru allar vefsíður líka með ákveðna merkingu efst, sem segja til um hverskonar skjal vafrinn á eiginlega að smíða úr textanum sem hann fær til sín.

Þessi beinagrind lítur svona út:

.. code-block:: html

    <!DOCTYPE html>
    <html>
        <head>
            <title></title>
        </head>
        <body>

        </body>
    </html>

Hérna kynnist þið fyrstu `HTML tögunum`_ ykkar, html, head, body og title. Þessi tög hafa öll mjög sérstakan tilgang sem við munum fara útí eftir örskamma stund, en ég ætla að byrja á að útskýra hvernig HTML skjöl eru send yfir internetið og hvernig vafrinn ykkar nær síðan að birta eitthverjar vefsíður út úr þessum HTML tögum.

.. todo::
    Strúktúr HTML taga

Þegar að HTML skjöl eru send yfir internetið eru þau send með samskiptahefð *(e. protocol)* sem kallast HTTP. Þegar að vafrinn byður netþjón fyrst um eitthverja vefsíðu, til dæmis þegar þið farið inn á *google.com* er fyrst sent það HTML skjal sem netþjónninn segir að eigi að vera sent fyrst, en það skjal heitir í nánast því öllum tilvikum *index.html*. Þegar að vafrinn er búinn að fá þessa vefsíðu frá netþjóninum byrjar hann á því að reyna að túlka hana. Þetta gerir vafrinn með því að skruna yfir skjalið og *rendera* það sem er inn í HTML tögunum á þann hátt sem er skilgreindur í skjalinu. Það sem þessi túlkur gerir fyrst er að lesa það sem er inni í <head> tögunum.

Það sem við geymum inni í <head> tögunum er það sem við viljum að vafrinn nái í áður en að restin af vefsíðunni, geymd inni í <body>, er *renderuð*. Þetta myndi til dæmis vera allskonar skriptur eða önnur mikilvæg skjöl sem vefsíðan þarf til að starfa á eðlilegann hátt

.. todo::
	Real-world dæmi um þetta

Nú þegar að við erum komin með þennan grunn, skulum við demba okkur dýpra í hvernig við getum notað HTML tög til þess að búa til vefi


.. _`Sublime Text`: http://www.sublimetext.com/
.. _`Firefox`: http://www.firefox.com/
.. _`Chrome`: http://www.chrome.com/
.. _`HTML tögunum`: http://www.w3schools.com/tags/
