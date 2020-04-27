from flask import Flask, jsonify
import os
from db import db

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from controllers.device_controller import devices

app.register_blueprint(devices, url_prefix='/devices')

# requests go here
@app.route('/')
def hello_world():
    return jsonify({"msg": "Homepage"})

if __name__ == '__main__' : 
    db.init_app(app)
    app.run(debug = True)