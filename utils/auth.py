import logging
import os
from datetime import datetime, timedelta

import jwt
from flask import request

if "JWT_SECRET" in os.environ:
    JWT_SECRET = os.environ.get("JWT_SECRET")
else:
    JWT_SECRET = "146d3e23cf5cfe60c6783ca89eae9474b75202e3105093e4"

def encode_token(user_data):
    try:
        user_data["exp"] = datetime.utcnow() + timedelta(days=1)
        token = jwt.encode(user_data, JWT_SECRET, algorithm="HS256")
        return token
    except Exception as e:
        logging.info("Failed to encode token: " + e)
        return None

def get_token():
    token = request.headers.get("Authorization")
    if token and len(token) > len("Bearer "):
        return token[len("Bearer "):]
    return None

def decode_token(token):
    return jwt.decode(token, JWT_SECRET, options={"require": ["exp", "card_number"]})
