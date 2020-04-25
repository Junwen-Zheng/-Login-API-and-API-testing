from flask import Flask
from flask_httpauth import HTTPBasicAuth
from flask_api import status
from json import dumps
from flask import request
from flask import Response

app = Flask(__name__)

auth = HTTPBasicAuth()

users = {
    "admin": "root",
}


