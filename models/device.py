from db import db

class Device(db.Model):
    __tablename__ = 'devices'
    id = db.Column(db.Integer, primary_key = True)
    hostName = db.Column(db.String(255))
    deviceType = db.Column(db.String(255))
    operatingSystem = db.Column(db.String(255))
    activeConnection = db.Column(db.Bool)
#   connectionTypes = db.Column(db.List) [1, 2]

def __init__(self, hostName, deviceType, operatingSystem, activeConnection):
        self.hostName = hostName
        self.deviceType = deviceType
        self.operatingSystem = operatingSystem
        self.activeConnection = activeConnection


