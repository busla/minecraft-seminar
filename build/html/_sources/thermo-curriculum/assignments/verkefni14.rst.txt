.. _thermo-assignment-14-solution:

Verkefni 14 - lausn
===================

.. code-block:: python

    # -*- coding: utf-8 -*-

    import os
    import glob  
    from datetime import datetime
    from tinydb import TinyDB, Query # Sækjum TinyDB módúluna
    import json
    import time

    db = TinyDB('db.json')

    def calculate_celsius(temp=None):
        if temp:
            return float(temp) / 1000.0
        return None

    def calculate_fahrenheit(temp=None):
        if temp:
            return temp * 1.8 + 32
        return None

    # Sækja hitastig úr gögnum
    def get_temp_from_data(data):
        temp_list = data[1].split('=')
        temp = temp_list[1]
        return temp

    # Lesa af skynjara
    def read_sensor(sensor):
        f = open(sensor, 'r')
        lines = f.read().splitlines()
        f.close()
        return lines

    # Finna af skynjara
    def find_sensor(sensor_id=None):
        base = '/sys/bus/w1/devices/'
        data_file = 'w1_slave'

        if sensor_id:
            sensor = os.path.join(base, sensor_id, data_file)
        
        else:
            try:
                folder = glob.glob(base + '28*')[0]            
            except IndexError:
                print('Enginn skynjari fannst!')
                return
            else:
                sensor = os.path.join(folder, data_file)

        return sensor


    # Hlaða inn rekla
    def mod_probe():
        os.system('modprobe w1-gpio')
        os.system('modprobe w1-therm')

    def start():
        mod_probe()
        #sensor = find_sensor('28-0000058e596b')
        sensor = find_sensor()

        while True:
            # Prentum út gögn frá skynjara
            data = read_sensor(sensor) # Setja gögn frá skynjara í breytu
            temp = get_temp_from_data(data) # Sækja hitastig úr gögnum. Hitastigið er í celsius * 1000

            celsius = calculate_celsius(temp) # Deilum með 1000 til að fá rétta tölu í celsius
            fahrenheit = calculate_fahrenheit(celsius) # Sendum rétt celsius hitastig í fahrenheit fallið til.

            db_data = {
                'fahrenheit': fahrenheit, 
                'celsius': celsius,
                'datetime': str(datetime.now()) # Breytum datetime gagnatípunni í streng.
            } 

            print(db_data)
            db.insert(db_data)
            time.sleep(3)


    start()