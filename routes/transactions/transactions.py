import json
from datetime import datetime

import requests
from flask import Blueprint
from utils.auth import token_required

transactions = Blueprint("transactions", __name__)

HEADERS = {
    "content-type": "application/json",
    "x-api-key": "PMAK-60c15befee0d380034366a96-0c571bc1bf1379aa80d655e94e4d9348f6"
}

@transactions.route("", methods=["GET"])
@token_required()
def get(user_data):
    transactions_data = requests.get("https://133b8793-d9dc-47b1-b2fe-4831f8859a7b.mock.pstmn.io//api/v1/gift-card/transactions", headers=HEADERS)
    if transactions_data.status_code != 200:
        return {"success": False, "message": "Falha ao comunicar com a API externa", "data": {"transactions_data": None}}, 200
    transactions_data = json.loads(transactions_data.text)
    key = 0
    for item in transactions_data:
        item["key"] = key
        item["transaction_date"] = datetime.strptime(item["transaction_date"], "%Y-%m-%d").strftime("%d/%m/%Y")
        key += 1
    return {"success": True, "message": "Transações lidas com sucesso", "data": {"transactions_data": transactions_data}}, 200
