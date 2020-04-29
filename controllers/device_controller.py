from flask import Blueprint, request, Response

from utils.db import db
from models.device import Device
from schemas.device_schema import device_schema, devices_schema

devices_blueprint = Blueprint('devices_blueprint', __name__)

@devices_blueprint.route('/', methods=['POST'])
def add_device():
    device_data = device_schema.load(request.json)
    new_device = Device(**device_data)
    db.session.add(new_device)
    db.session.commit()
    return device_schema.dump(new_device)

@devices_blueprint.route('/', methods=['GET'])
def get_devices():
    all_devices = Device.query.all()
    for device in all_devices:
            device.update()
    devices_data = devices_schema.dumps(all_devices)
    response = Response(devices_data, status=200, mimetype='application/json')
    return response
