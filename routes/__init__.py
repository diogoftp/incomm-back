from flask import Flask
from flask_cors import CORS

from routes.login.login import login

api = Flask(__name__)
CORS(api)

api.register_blueprint(login, url_prefix="/api/login")
