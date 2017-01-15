from tinydb import TinyDB, Query

db = TinyDB('db.json')

for item in db.all():
    print(item)