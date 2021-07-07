import os
from flask import Flask
from flask_cors import CORS

from routes.login.login import login
from routes.token.token import token
from routes.info.info import info

api = Flask(__name__)
CORS(api)

if "ENV" in os.environ:
    ENVIRONMENT = os.environ.get("ENVIRONMENT")
else:
    ENVIRONMENT = "local"

api.register_blueprint(login, url_prefix="/api/login")
api.register_blueprint(token, url_prefix="/api/token")
api.register_blueprint(info, url_prefix="/api/info")
