from flask import Flask
from flask_cors import CORS
from flask_restx import Api

from routes.info.info import api as info
from routes.login.login import api as login
from routes.token.token import api as token
from routes.transactions.transactions import api as transactions

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config["RESTX_MASK_SWAGGER"] = False

api = Api (
    title="GiftCards-API",
    version="1.0",
    description="API Gift Cards",
    doc ="/api",
    prefix="/api"
)
api.init_app(app)

api.add_namespace(login, path="/login")
api.add_namespace(token, path="/token")
api.add_namespace(info, path="/info")
api.add_namespace(transactions, path="/transactions")
