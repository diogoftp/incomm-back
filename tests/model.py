from datetime import datetime, timedelta

import bcrypt
import jwt
from bson import ObjectId

MOCKED_JWT_SECRET = "dummy"

card_object = {
    "_id": ObjectId("60e66d6bb137cf457ca330d2"),
    "number": 1111111111111111,
    "message": "Alguma mensagem",
    "balance": 1500.0,
    "expiration": datetime.strptime("2022-05-05T00:00:00.000Z", "%Y-%m-%dT%H:%M:%S.%fZ"),
    "password": bcrypt.hashpw("123456".encode("utf-8"), bcrypt.gensalt())
}

expired_date = datetime.utcnow() + timedelta(days=-500)

expired_token = "Bearer " + jwt.encode({"card_number": card_object["number"], "exp": expired_date}, MOCKED_JWT_SECRET, algorithm="HS256").decode("utf-8")

valid_date = datetime.utcnow() + timedelta(days=5)

valid_token = "Bearer " + jwt.encode({"card_number": card_object["number"], "exp": valid_date}, MOCKED_JWT_SECRET, algorithm="HS256").decode("utf-8")
