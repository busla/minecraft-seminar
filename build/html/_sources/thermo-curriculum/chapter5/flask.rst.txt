Kafli 5
========

.. code-block:: python

    pip3 install flask --user
    pip3 install flask-cors --user


.. code-block:: python

    # -*- coding: utf-8 -*-

    from flask import Flask, jsonify
    from flask_cors import CORS, cross_origin
    from tinydb import TinyDB

    app = Flask(__name__)
    CORS(app)

    db = TinyDB('db.json')

    @app.route('/entries')
    def get_entries():    

        return jsonify(data=db.all())


    @app.route('/')
    def home():    
        return 'Velkominn!', 200


    if __name__ == '__main__':
            
        app.run(debug=True, host='0.0.0.0')    