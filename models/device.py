from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

Device = {
  name: "Alan's phone",
  type: "phone",
  operatingSystem: "Android",
  connectionTypes: [{
    type: "ethernet",
    macAddress: "00:1B:44:11:3A:B7",
    ipAddress: null
  },
  {
    type: "wifi",
    macAddress: "00:1D:37:12:3B:A9"
  }],
  connected: null
}