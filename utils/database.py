import os

from pymongo import MongoClient

DEFAULT_DB_URI = "mongodb://localhost:5123/"
DEFAULT_DB_NAME = "GiftCards"

def get_db_name():
    if "DB_NAME" in os.environ:
        return os.environ.get("DB_NAME")
    return DEFAULT_DB_NAME

def get_db_uri():
    if "DB_URI" in os.environ:
        return  os.environ.get("DB_URI")
    return DEFAULT_DB_URI

database = MongoClient(get_db_uri())[get_db_name()]
