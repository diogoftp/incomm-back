"""Database related functions and constants
"""

import os

from pymongo import MongoClient

DEFAULT_DB_URI = "mongodb://localhost:5123/"
DEFAULT_DB_NAME = "GiftCards"

def get_db_name():
    """Tries to get the database name from environment

    Returns:
        string: the database name

    """
    if "DB_NAME" in os.environ:
        return os.environ.get("DB_NAME")
    return DEFAULT_DB_NAME

def get_db_uri():
    """Tries to get the database URI from environment

    Returns:
        string: the database URI

    """
    if "DB_URI" in os.environ:
        return  os.environ.get("DB_URI")
    return DEFAULT_DB_URI

database = MongoClient(get_db_uri())[get_db_name()]
