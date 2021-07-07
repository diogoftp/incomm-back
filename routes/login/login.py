from flask import Blueprint, request
login = Blueprint("login", __name__)

@login.route("", methods=["POST"])
def post():
    data = request.json
    card_number = data["card_number"]
    password = data["password"]
    return {"success": True, "message": "Login realizado com sucesso", "data": {"token": "TOKEN"}}, 200
