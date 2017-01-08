.. _thermo-assignment-13-solution:

Verkefni 13 - lausn
===================

.. code-block:: python

    from datetime import datetime
    import random
    import uuid

    class Hitakerfi:

        def __init__(self):
            self.dagsetning = self.setja_dagsetningu()
            self.id = self.setja_id()
            self.hitastig = self.finna_hita()
            self.skynjari = self.velja_skynjara()

        def reikna_fahrenheit(self):
            fahrenheit = (self.hitastig - 32) / 1.8
            return 'Hitinn er {}°F'.format(fahrenheit) 

        def setja_dagsetningu(self):        
            return datetime.now()

        def finna_hita(self):
            return random.randint(-50, 50)

        def velja_skynjara(self):
            skynjari = ['stofa', 'baðherbergi', 'svefnherbergi', 'bílskúr']
            return random.choice(skynjari)

        def setja_id(self):
            return uuid.uuid4()

    h1 = Hitakerfi()
    print(h1.dagsetning)
    print(h1.id)
    print(h1.hitastig)
    print(h1.skynjari)
    print(h1.reikna_fahrenheit())