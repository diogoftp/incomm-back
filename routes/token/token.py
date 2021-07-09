from flask_restx import Resource
from utils.auth import decode_token, encode_token, get_token, token_required

from model import responses

from .model import api, default_return


@api.route("/refresh")
@api.doc(responses = responses, security = "jwt")
class Token(Resource):
    @api.marshal_list_with(default_return)
    @token_required()
    def get(self, user_data):
        token = get_token()
        user_data = decode_token(token)
        token = encode_token(user_data)
        return {"success": True, "message": "Token atualizado com sucesso", "data": {"token": token}}, 200
