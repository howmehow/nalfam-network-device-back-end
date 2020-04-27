from device import Device
from app import ma 

class DeviceSchema(ma.ModelSchema):
    class Meta:
        model = Device