import logging
import os
from datetime import datetime, timedelta
from functools import wraps

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

def token_required():
    def validate_token(f):
        @wraps(f)
        def decorator(*args, **kwargs):
            token = get_token()
            if not token:
                return {"success": False, "message": "Token não encontrado", "data": {}}, 401
            try:
                user_data = decode_token(token)
            except jwt.exceptions.ExpiredSignatureError:
                return {"success": False, "message": "Token expirado", "data": {}}, 401
            except (jwt.exceptions.DecodeError, jwt.exceptions.InvalidSignatureError, jwt.exceptions.InvalidKeyError, jwt.exceptions.InvalidAlgorithmError, jwt.exceptions.MissingRequiredClaimError):
                return {"success": False, "message": "Erro na validação do token", "data": {}}, 401
            except jwt.exceptions.InvalidTokenError:
                return {"success": False, "message": "Token inválido", "data": {}}, 401
            return f(user_data, *args, **kwargs)
        return decorator
    return validate_token
