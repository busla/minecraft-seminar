# -*- coding: utf-8 -*-
from datetime import datetime
import json
import time
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/entry/add/<temp_value>')
def add_entry(temp_value):
    entry = Entry(temp_value=float(temp_value), temp_date=datetime.utcnow())
    db.session.add(entry)
    db.session.commit()
    return 'bætti við', 200

@app.route('/entries')
def show_entry():
    entry_list = []
    entries = Entry.query.all()
    for entry in entries:
        entry_list.append({
            'id': entry.id,
            'temp_value': entry.temp_value,
            'temp_date': entry.temp_date
            })    
    return jsonify(data=entry_list)

@app.route('sensor/start')
def sensor_start():

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
    

@app.route('/')
def home():    
    return 'Hæ', 200


if __name__ == '__main__':
        
    app.run(debug=True)    