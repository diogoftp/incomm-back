"""Endpoint for gift cards information
"""

from flask_restx import Resource
from utils.auth import token_required
from utils.database import database

from model import responses

from .model import api, default_return


@api.route("")
@api.doc(responses = responses, security = "jwt")
class Info(Resource):
    @api.marshal_list_with(default_return)
    @token_required()
    def get(self, user_data):
        """GET method for gift card information

        Args:
            user_data (obj): user data received from the "token_required" decorator
        
        Returns:
            tuple (obj, int): response information and HTTP status code
        """
        card_number = int(user_data["card_number"])
        card = database.gift_cards.find_one({"number": card_number}, {"_id": False, "password": False})
        if not card:
            return {"success": False, "message": "Falha ao ler dados do cartão", "data": {"card_data": None}}, 200
        card["expiration"] = card["expiration"].strftime("%d/%m/%Y") # Datetime to string since it is not JSON serializable
        return {"success": True, "message": "Dados do cartão lidos com sucesso", "data": {"card_data": card}}, 200
