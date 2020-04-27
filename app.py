from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
from models.device import Device

import os
from db import db


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# requests go here
@app.route('/')
def hello_world():
    return jsonify({"hostName": "Alan's phone", "deviceType": "phone", "operatingSystem": "Android"})

@app.route('/device')
def device():
    return device.json()


if __name__ == '__main__' : 
    db.init_app(app)
    app.run(debug = True)