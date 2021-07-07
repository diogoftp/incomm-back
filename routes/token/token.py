import jwt
from flask import Blueprint, request
from utils.auth import encode_token, get_token, decode_token

token = Blueprint("token", __name__)

@token.route("/refresh", methods=["GET"])
def get():
    token = get_token()
    if not token:
        return {"success": False, "message": "Token não encontrado", "data": {}}, 401
    try:
        user_data = decode_token(token)
    except jwt.exceptions.ExpiredSignatureError:
        return {"success": False, "message": "Token expirado", "data": {}}, 200
    except (jwt.exceptions.DecodeError, jwt.exceptions.InvalidSignatureError, jwt.exceptions.InvalidKeyError, jwt.exceptions.InvalidAlgorithmError, jwt.exceptions.MissingRequiredClaimError):
        return {"success": False, "message": "Erro na validação do token", "data": {}}, 401
    except jwt.exceptions.InvalidTokenError:
        return {"success": False, "message": "Token inválido", "data": {}}, 401
    token = encode_token(user_data)
    return {"success": True, "message": "Token atualizado com sucesso", "data": {"token": token.decode("utf-8")}}, 200
