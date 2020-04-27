from ma import ma
from models.device import Device

class DeviceSchema(ma.ModelSchema):
    class Meta:
        model = Device
#fields = ('id', 'hostName', 'deviceType', 'operatingSystem', 'activeConnection')
device_schema = DeviceSchema()
devices_schema = DeviceSchema(many=True)