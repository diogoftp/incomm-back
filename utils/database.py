import os
from pymongo import MongoClient

if "DB_URI" in os.environ:
    DB_URI = os.environ.get("DB_URI")
else:
    DB_URI = "mongodb://localhost:5123/"

if "DB_NAME" in os.environ:
    DB_NAME = os.environ.get("DB_NAME")
else:
    DB_NAME = "GiftCards"

database = MongoClient(DB_URI)[DB_NAME]
