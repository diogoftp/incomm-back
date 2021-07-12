"""Models for "/login" endpoint
"""

from flask_restx import Namespace, fields

from model import authorizations, default_return_model

api = Namespace("Login", description="User login", authorizations=authorizations)

default_return = api.model("Return", default_return_model)

post_body = api.model("Login", {
    "card_number": fields.Integer(description="Gift card number", required=True, example="1111111111111111"),
    "password": fields.String(description="Password", required=True, example="123456")
})
