.. _terminal:

Terminal
===============

Í *Terminal* notum við aðgerðir sem tengjast ekki Python á neinn hátt. *Terminal* mun verða ykkar tryggasti vinur þegar þið byrjið að forrita síðar. Til að framkvæma aðgerðir í stýrikerfinu getum við nota glugga viðmót eða texta viðmót. Í glugga viðmótinu notum við *File Manager* til að skoða skrár, búa til möppur, opna forrit, o.s.f.v. Í texta viðmótinu gerum við sömu hluti en við skrifum skipanir til að framkvæma þær. Rétt eins og við höfum við að skrifa skipunina *python3* til að opna Python skelina.

Í texta viðmótinu getum við framkvæmt fleiri aðgerðir en í glugga viðmótinu. Hér fyrir ofan notum við aðgerðina *cd* sem fer með okkur í notandamöppuna okkar. Síðan notum við *mkdir (make directory)* til að búa til nýja möppu. Skipunin *ls* sýnir okkur hvað er í henni:

.. code-block:: bash
    
    $ ls

Til að fara inn í einhverja af þessum möppuna notarðu *cd* og nafnið á möppunni.

.. code-block:: bash

    $ cd Documents
    $ ls

Passaðu þig á stórum og litlum stöfum, þeir skipta máli. Mappan *Documents* er ekki það sama og mappan *documents*. Til að fara aftur niður um möppu notiði *cd*, bil og tveir punktar.

.. code-block:: bash

    $ cd ..
    $ ls


Búum til nýja möppu og tóma skrá.

.. code-block:: bash

    $ mkdir mappa
    $ cd mappa    
    $ touch tomskra.txt    