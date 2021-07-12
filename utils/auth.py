"""Authentications related functions and constants
"""

import os
from datetime import datetime, timedelta
from functools import wraps

import bcrypt
import jwt
from flask import request

DEFAULT_JWT_SECRET = "146d3e23cf5cfe60c6783fa89eve2474b75202e3105093e4"

def get_jwt_secret():
    """Tries to get the JWT secret from environment

    Returns:
        string: the JWT secret

    """
    if "JWT_SECRET" in os.environ:
        return os.environ.get("JWT_SECRET")
    return DEFAULT_JWT_SECRET

JWT_SECRET = get_jwt_secret()

def encode_token(user_data):
    """Encodes a JWT token with the user data

    Args:
        user_data (obj): the user data

    Returns:
        string: the JWT token

    """
    user_data["exp"] = datetime.utcnow() + timedelta(days=3)
    token = jwt.encode(user_data, JWT_SECRET, algorithm="HS256")
    return token.decode("utf-8")

def get_token():
    """Gets a JWT token from a request header

    Returns:
        string: the JWT token

    """
    token = request.headers.get("Authorization")
    if token and len(token) > len("Bearer "):
        return token[len("Bearer "):]
    return None

def decode_token(token):
    """Decodes a JWT token

    Args:
        token (string): a JWT token

    Returns:
        obj: the decoded JWT token

    """
    return jwt.decode(token, JWT_SECRET, options={"require": ["exp", "card_number"]})

def token_required():
    """Decorator that checks and validates a JWT token on protected endpoints

    Args:
        f (function): the decorated function

    Returns:
        function: the decorated function or non-authorized messages

    """
    def validate_token(f):
        @wraps(f)
        def decorator(self, *args, **kwargs):
            token = get_token()
            if not token:
                return {"success": False, "message": "Token não encontrado", "data": {}}, 401
            try:
                user_data = decode_token(token)
            except jwt.exceptions.ExpiredSignatureError:
                return {"success": False, "message": "Token expirado", "data": {}}, 401
            except (jwt.exceptions.InvalidTokenError, jwt.exceptions.DecodeError, jwt.exceptions.InvalidSignatureError, jwt.exceptions.InvalidKeyError, jwt.exceptions.InvalidAlgorithmError, jwt.exceptions.MissingRequiredClaimError):
                return {"success": False, "message": "Erro na validação do token", "data": {}}, 401
            return f(self, user_data, *args, **kwargs)
        return decorator
    return validate_token

def check_password(password, hashed_password):
    """Checks the user password against its hashed password from database

    Args:
        password (string): the user's password
        hashed_password (bytes): the stored user's password

    Returns:
        bool: True if successful, False otherwise

    """
    if bcrypt.hashpw(password.encode("utf-8"), hashed_password) == hashed_password:
        return True
    return False
