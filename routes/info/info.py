from flask_restx import Resource
from utils.auth import token_required
from utils.database import database

from model import responses

from .model import api, default_return


@api.route("")
@api.doc(responses = responses, security = "jwt")
class Token(Resource):
    @api.marshal_list_with(default_return)
    @token_required()
    def get(self, user_data):
        card_number = int(user_data["card_number"])
        card = database.gift_cards.find_one({"number": card_number}, {"_id": False, "password": False})
        if not card:
            return {"success": False, "message": "Falha ao ler dados do cartão", "data": {"card_data": None}}, 200
        card["expiration"] = card["expiration"].strftime("%d/%m/%Y")
        return {"success": True, "message": "Dados do cartão lidos com sucesso", "data": {"card_data": card}}, 200
