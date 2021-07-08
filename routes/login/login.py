from flask import Blueprint, request
from utils.auth import check_password, encode_token
from utils.database import database

login = Blueprint("login", __name__)

@login.route("", methods=["POST"])
def post():
    data = request.json
    card_number = int(data["card_number"])
    password = data["password"]
    card = database.gift_cards.find_one({"number": card_number})
    if not card:
        return {"success": False, "message": "Cartão não encontrado", "data": {"token": None}}, 200
    if not check_password(password, card["password"]):
        return {"success": False, "message": "Senha incorreta", "data": {"token": None}}, 200
    token = encode_token({"card_number": card["number"]})
    if not token:
        return {"success": False, "message": "Falha ao realizar o login", "data": {"token": None}}, 200
    return {"success": True, "message": "Login realizado com sucesso", "data": {"token": token.decode("utf-8")}}, 200
