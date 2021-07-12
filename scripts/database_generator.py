"""This script generates initial data for the MongoDB database
"""

import os
from datetime import datetime

import bcrypt
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

gift_cards = [
    {
        "number": 1234567890123456,
        "message": "Alguma mensagem",
        "balance": 1500.0,
        "expiration": datetime.strptime("05/05/2022", "%d/%m/%Y"),
        "password": bcrypt.hashpw("123abc".encode("utf-8"), bcrypt.gensalt())
    },
    {
        "number": 1111111111111111,
        "message": "Outra mensagem",
        "balance": 2000.0,
        "expiration": datetime.strptime("02/06/2022", "%d/%m/%Y"),
        "password": bcrypt.hashpw("123456".encode("utf-8"), bcrypt.gensalt())
    }
]

transactions = [
    {
        "card_number": 1234567890123456,
        "store_identification": "ecommerce",
        "transaction_date": datetime.strptime("01/01/2021", "%d/%m/%Y"),
        "transaction_type": "redeem",
        "transaction_value": -100.0
    },
    {
        "card_number": 1234567890123456,
        "store_identification": "ecommerce",
        "transaction_date": datetime.strptime("01/02/2021", "%d/%m/%Y"),
        "transaction_type": "redeem",
        "transaction_value": -100.0
    },
    {
        "card_number": 1234567890123456,
        "store_identification": "ecommerce",
        "transaction_date": datetime.strptime("01/03/2021", "%d/%m/%Y"),
        "transaction_type": "reload",
        "transaction_value": 100.0
    },
    {
        "card_number": 1234567890123456,
        "store_identification": "ecommerce",
        "transaction_date": datetime.strptime("01/04/2021", "%d/%m/%Y"),
        "transaction_type": "reload",
        "transaction_value": 100.0
    },
    {
        "card_number": 1234567890123456,
        "store_identification": "Loja Shopping",
        "transaction_date": datetime.strptime("01/04/2021", "%d/%m/%Y"),
        "transaction_type": "redeem",
        "transaction_value": -100.0
    },
    {
        "card_number": 1234567890123456,
        "store_identification": "Loja Shopping",
        "transaction_date": datetime.strptime("01/05/2021", "%d/%m/%Y"),
        "transaction_type": "redeem",
        "transaction_value": -100.0
    },
    {
        "card_number": 1234567890123456,
        "store_identification": "Loja Shopping",
        "transaction_date": datetime.strptime("01/06/2021", "%d/%m/%Y"),
        "transaction_type": "reload",
        "transaction_value": 100.0
    },
    {
        "card_number": 1234567890123456,
        "store_identification": "Loja Shopping",
        "transaction_date": datetime.strptime("01/07/2021", "%d/%m/%Y"),
        "transaction_type": "activation",
        "transaction_value": 400.0
    },
    # Second card
    {
        "card_number": 1111111111111111,
        "store_identification": "ecommerce",
        "transaction_date": datetime.strptime("22/01/2021", "%d/%m/%Y"),
        "transaction_type": "redeem",
        "transaction_value": -100.0
    },
    {
        "card_number": 1111111111111111,
        "store_identification": "ecommerce",
        "transaction_date": datetime.strptime("22/02/2021", "%d/%m/%Y"),
        "transaction_type": "redeem",
        "transaction_value": -100.0
    },
    {
        "card_number": 1111111111111111,
        "store_identification": "ecommerce",
        "transaction_date": datetime.strptime("22/03/2021", "%d/%m/%Y"),
        "transaction_type": "reload",
        "transaction_value": 100.0
    },
    {
        "card_number": 1111111111111111,
        "store_identification": "ecommerce",
        "transaction_date": datetime.strptime("22/04/2021", "%d/%m/%Y"),
        "transaction_type": "reload",
        "transaction_value": 100.0
    },
    {
        "card_number": 1111111111111111,
        "store_identification": "Loja Shopping",
        "transaction_date": datetime.strptime("22/04/2021", "%d/%m/%Y"),
        "transaction_type": "redeem",
        "transaction_value": -100.0
    },
    {
        "card_number": 1111111111111111,
        "store_identification": "Loja Shopping",
        "transaction_date": datetime.strptime("22/05/2021", "%d/%m/%Y"),
        "transaction_type": "redeem",
        "transaction_value": -100.0
    },
    {
        "card_number": 1111111111111111,
        "store_identification": "Loja Shopping",
        "transaction_date": datetime.strptime("22/06/2021", "%d/%m/%Y"),
        "transaction_type": "reload",
        "transaction_value": 100.0
    },
    {
        "card_number": 1111111111111111,
        "store_identification": "Loja Shopping",
        "transaction_date": datetime.strptime("22/07/2021", "%d/%m/%Y"),
        "transaction_type": "activation",
        "transaction_value": 400.0
    }
]

database.drop_collection("gift_cards")
database.drop_collection("transactions")
database.gift_cards.create_index("number", unique=True)
database.gift_cards.insert_many(gift_cards)
database.transactions.insert_many(transactions)
print("Success")
