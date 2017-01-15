# -*- coding: utf-8 -*-

import os
import glob
import time


def mod_probe():
    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')

def calculate_celsius(temp=None):
    if temp:
        return float(temp) / 1000.0

    return None

def calculate_fahrenheit(temp=None):
    if temp:
        return temp * 1.8 + 32
    return None

def read_sensor_data(device_file):
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp(device_file):
    lines = read_sensor_data(device_file)

    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_sensor_data()

    equals_pos = lines[1].find('t=')
    
    if equals_pos != -1:
        temp = lines[1][equals_pos+2:]
        
        celsius = calculate_celsius(temp)
        fahrenheit = calculate_fahrenheit(celsius)

        return {'fahrenheit': fahrenheit, 'celsius': celsius}

    return 'Eitthvað fór úrskeiðis'

def get_temp():
    mod_probe()

    base_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob(base_dir + '28*')[0]
    device_file = device_folder + '/w1_slave'
     
        
    while True:
        print(read_temp(device_file))  
        time.sleep(1)

if __name__ == '__main__':
    get_temp()
