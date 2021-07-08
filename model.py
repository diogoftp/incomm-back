from flask_restx import fields

responses = {
    200: "Success",
    400: "Bad Request",
    401: "Unauthorized",
    500: "Internal Server Error"
}

default_return_model = {
    "success": fields.Boolean(required=True, description="Response status"),
    "message": fields.String(required=True, description="Response message"),
    "data": fields.Raw(required=True, description="Response data"),
}

authorizations = {
    "jwt": {
        "type": "apiKey",
        "name": "Authorization",
        "in": "header"
    }
}
