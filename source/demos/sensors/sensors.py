import os
import glob
import time
from SensorController import TempSensorController, Temperature

if __name__ == "__main__":

    #create temp sensor controller, put your controller Id here
    # look in "/sys/bus/w1/devices/" after running
    #  sudo modprobe w1-gpio
    #  sudo modprobe w1-therm
    
    tempcontrol = TempSensorController("28-0000058e596b", 1)

    try:
        print("Starting temp sensor controller")
        #start up temp sensor controller
        tempcontrol.start()
        #loop forever, wait for Ctrl C
        while(True):
            print(tempcontrol.temperature.celsius())
            print(tempcontrol.temperature.fahrenheit())
            time.sleep(5)

    #Ctrl C
    except KeyboardInterrupt:
        print("Cancelled")
   
    #Error
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

    #if it finishes or Ctrl C, shut it down
    finally:
        print("Stopping temp sensor controller")
        #stop the controller
        tempcontrol.stopController()
        #wait for the tread to finish if it hasn't already
        tempcontrol.join()
       
    print("Done")
    
    #get_temp()