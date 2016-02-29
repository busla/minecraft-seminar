import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
print("LED is on")
GPIO.output(21, GPIO.HIGH)
time.sleep(3)
print("LED is off")
GPIO.output(21, GPIO.LOW)
