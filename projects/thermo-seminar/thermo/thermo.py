from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///Users/levy/code/minecraft-seminar/projects/thermo-seminar/thermo/database.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temp_date = db.Column(db.DateTime)
    temp_value = db.Column(db.Float)

    def __init__(self, temp_date, temp_value):
        self.temp_date = temp_date
        self.temp_value = temp_value


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

@app.route('/')
def home():    
    return 'Hæ', 200


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=5001)    