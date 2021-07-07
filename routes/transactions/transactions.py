from flask import Blueprint
from utils.auth import token_required

from datetime import datetime, timedelta

transactions = Blueprint("transactions", __name__)

transactions_data = [
    {
        "key": "1",
        "type": "withdrawl",
        "date": "06/07/2021",
        "value": 500.0,
        "identification": "E-Commerce"
    },
    {
        "key": "2",
        "type": "activation",
        "date": "05/07/2021",
        "value": -100.0,
        "identification": "Loja Shopping"
    },
    {
        "key": "3",
        "type": "cancellation",
        "date": "22/06/2021",
        "value": -100.0,
        "identification": "Loja Shopping"
    }
]

@transactions.route("", methods=["GET"])
@token_required()
def get(user_data):
    # TODO: get from database
    return {"success": True, "message": "Login realizado com sucesso", "data": {"transactions_data": transactions_data}}, 200
