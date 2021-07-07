from flask import Blueprint
from utils.auth import token_required

from datetime import datetime, timedelta

info = Blueprint("info", __name__)

card_data = {
    "number": 1234567890123456,
    "message": "Alguma mensagem",
    "balance": 1000.00,
    "expiration": (datetime.utcnow() + timedelta(days=1)).strftime("%d/%m/%Y")
}

@info.route("", methods=["GET"])
@token_required()
def get(user_data):
    # TODO: get from database
    return {"success": True, "message": "Login realizado com sucesso", "data": {"card_data": card_data}}, 200
