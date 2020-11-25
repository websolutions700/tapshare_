from flask import Flask
from flask_pymongo import PyMongo
from pyrebase import pyrebase

app = Flask(__name__)
# app.config.from_object(Config)

firebaseConfig = {
    'apiKey': "AIzaSyDrf99FG54ry52s7ypPTQ8kPui67aHNBuc",
    'authDomain': "testdb-15f70.firebaseapp.com",
    'databaseURL': "https://testdb-15f70.firebaseio.com",
    'projectId': "testdb-15f70",
    'storageBucket': "testdb-15f70.appspot.com",
    'messagingSenderId': "571734547670",
    'appId': "1:571734547670:web:41034f55a2f48b848a3d77"
}

firebase = pyrebase.initialize_app(firebaseConfig);

auth = firebase.auth()
db = firebase.database()
storage = firebase.storage()

from app import routes