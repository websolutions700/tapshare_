from flask import Flask
# from flask_pymongo import PyMongo
from pyrebase import pyrebase

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
# app.config.from_object(Config)

firebaseConfig = {
    'apiKey': "AIzaSyBgkIqbQg48LICpActIi2GSoFMbcFF-Hqg",
    'authDomain': "tap-share-1.firebaseapp.com",
    'databaseURL': "https://tap-share-1.firebaseio.com/",
    'projectId': "tap-share-1",
    'storageBucket': "tap-share-1.appspot.com",
    'messagingSenderId': "893270889227",
    'appId': "1:893270889227:web:47ab47ff948ea7e68d880e",
    'measurementId' : "G-XKJ11ET6LL"
}

firebase = pyrebase.initialize_app(firebaseConfig);

auth = firebase.auth()
db = firebase.database()
storage = firebase.storage()

from app import routes