TinyDB
========


Keyrðu hitaforritið úr *verkefni14* og láttu það ganga í dágóðan tíma. Taktu utan um skynjarann af og til svo þú fáir breytilegan hita í gagnagrunninn.

Búðu til skrána *verkefni15.py*. Í henni munum við skrifa kóða til að sækja gögn úr grunninum.

Áður en við byrjum skulum við sækja TinyDB sem er gagnagrunnurinn sem við munum nota.

.. code-block:: python

    pip install tinydb --user

    
Byrjum á að sækja allar færslur:

.. code-block:: python

    from tinydb import TinyDB, Query
    
    db = TinyDB('db.json')

    print(db.all()) # Prentum út allar færslur í grunninum.


Prentum út allar færslur línu fyrir línu.

.. code-block:: python

    from tinydb import TinyDB, Query
    
    db = TinyDB('db.json')

    for item in db.all():
        print(item)


Sækjum færslur sem standast samanburðarfullyrðingar.

.. code-block:: python

    from tinydb import TinyDB, Query
    
    db = TinyDB('db.json')

    Temp = Query()

    results = db.search(Temp.celsius > 23.7) # Sækja allar færslur þar sem celsius er hærri en 23.7
    print(results)    


Eftirfarandi skilar sömu niðurstöðu með öðru verkfæri:

.. code-block:: python

    from tinydb import TinyDB, where # Sækjum where    

    db = TinyDB('db.json')

    results = db.search(where('celsius') > 23.7)
    print(results)



Sækjum færslur á milli tveggja tímasetninga:

.. code-block:: python

    from tinydb import TinyDB, where
    from datetime import datetime, timedelta # Sækjum datetime og timedelta

    db = TinyDB('db.json')

    date_from = datetime.now()
    date_to = datetime.now() - timedelta(minutes=2)
    results = db.search((where('datetime') < str(date_from)) & (where('datetime') > str(date_to)))
    print(results)    



Kíktu á TinyDB_ handbókina til að skoða allar aðgerðir.

.. _TinyDB: http://tinydb.readthedocs.io/en/latest/usage.html