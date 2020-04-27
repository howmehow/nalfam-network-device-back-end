from flask import Blueprint, request

from db import db
from models.device import Device
from schemas.deviceSchema import DeviceSchema, device_schema, devices_schema

devices = Blueprint('devices', __name__)

@devices.route('/devices', methods=['POST'])
def add_device():
    hostName = request.json['hostName']
    deviceType = request.json['deviceType']
    operatingSystem = request.json['operatingSystem']
    activeConnection = request.json['activeConnection']
    
    new_device = Device(hostName, deviceType, operatingSystem, activeConnection)
    db.session.add(new_device)
    db.session.commit()

    return device_schema.dump(new_device)

@devices.route('/', methods=['GET'])
def get_devices():
    all_devices = Device.query.all()
    return devices_schema.dumps(all_devices)

