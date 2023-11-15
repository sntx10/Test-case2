from pymongo import MongoClient

client = MongoClient('mongodb://db:27017/')
db = client.forms_db
forms_collection = db.forms
