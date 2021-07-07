from flask import Blueprint, request
from utils.auth import encode_token

login = Blueprint("login", __name__)

@login.route("", methods=["POST"])
def post():
    data = request.json
    card_number = data["card_number"]
    password = data["password"]
    # TODO: verify credentials
    token = encode_token({"card_number": card_number})
    if not token:
        return {"success": False, "message": "Falha ao realizar o login", "data": {"token": None}}, 500
    return {"success": True, "message": "Login realizado com sucesso", "data": {"token": token.decode("utf-8")}}, 200
