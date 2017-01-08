GPIO (Gagnapinnar)
==================

.. image:: gpio-pins.png

.. image:: gpio-led.png

.. image:: gpio-pinout.png


.. code-block:: python
    import RPi.GPIO as GPIO
    import time

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21, GPIO.OUT)


    GPIO.output(21, GPIO.LOW)
    print("Kveikt")
    GPIO.output(21, GPIO.HIGH)
    time.sleep(1)
    print("Slökkt")
    GPIO.output(21, GPIO.LOW)
    time.sleep(1)
