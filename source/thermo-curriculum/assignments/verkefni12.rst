.. _thermo-assignment-12-solution:

Verkefni 12 - lausn
===================

.. code-block:: python

    from datetime import datetime
    import random

    """
    def reikna_celsius(hiti=None):
        return hiti * 1.8 + 32

    def reikna_fahrenheit(hiti=None):
        return (hiti - 32) / 1.8
    """

    def finna_dags():
        return datetime.now()

    def finna_hita():
        return random.randint(-50, 50)

    def velja_skynjara():
        skynjari = ['stofa', 'baðherbergi', 'svefnherbergi', 'bílskúr']
        return random.choice(skynjari)

    def reikna_hitastig(hiti=None, tegund='c'):

        if tegund == 'f':
            return reikna_fahrenheit(hiti)
        elif tegund == 'c':
            return reikna_celsius(hiti)
        else:
            return 'Óþekkt hitategund: {}'.format(tegund)


    def hitavel():
        hitalisti = []
        hitasafn = {}

        for x in range(1, 100):
            hitasafn = {
                'id': x,
                'dags': finna_dags(),
                'hiti': finna_hita(),
                'skynjari': velja_skynjara()
            }
            hitalisti.append(hitasafn)

        return hitalisti

    print(hitavel())
