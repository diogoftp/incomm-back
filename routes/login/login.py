"""Endpoint for login operations
"""

from flask_restx import Resource, reqparse
from utils.auth import check_password, encode_token
from utils.database import database

from model import responses

from .model import api, default_return, post_body


@api.route("")
@api.doc(responses = responses)
class Login(Resource):
    @api.marshal_list_with(default_return)
    @api.doc(body = post_body)
    def post(self):
        """POST method for login

        Returns:
            tuple (obj, int): response information and HTTP status code
        """
        parser = reqparse.RequestParser()
        parser.add_argument("card_number", required=True, type=int)
        parser.add_argument("password", required=True, type=str)
        args = parser.parse_args(strict=True)
        card_number = args.get("card_number")
        password = args.get("password")
        card = database.gift_cards.find_one({"number": card_number})
        if not card:
            return {"success": False, "message": "Cartão não encontrado", "data": {"token": None}}, 200
        if not check_password(password, card["password"]):
            return {"success": False, "message": "Senha incorreta", "data": {"token": None}}, 200
        token = encode_token({"card_number": card["number"]})
        return {"success": True, "message": "Login realizado com sucesso", "data": {"token": token}}, 200
