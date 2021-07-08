from flask_restx import Namespace

from model import authorizations, default_return_model

api = Namespace("Gift Card Info", description="Gift card informations", authorizations=authorizations)

default_return = api.model("Return", default_return_model)
