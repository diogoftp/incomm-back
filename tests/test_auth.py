import os
import unittest
from unittest.mock import patch

from routes import app as test_app
from utils.auth import DEFAULT_JWT_SECRET, get_jwt_secret

from .model import MOCKED_JWT_SECRET, expired_token


@patch("utils.auth.JWT_SECRET", MOCKED_JWT_SECRET)
class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = test_app.test_client()

    def test_token_validation_error(self):
        request = self.app.get("/api/token/refresh", headers={"Authorization": "Bearer fdsa"})
        self.assertEqual(401, request.status_code)
        self.assertIn("success", request.json)
        self.assertIn("data", request.json)
        self.assertIn("message", request.json)
        self.assertEqual(False, request.json["success"])
        self.assertDictEqual(request.json["data"], {})

    def test_token_not_found(self):
        request = self.app.get("/api/token/refresh", headers={"Authorization": ""})
        self.assertEqual(401, request.status_code)
        self.assertIn("success", request.json)
        self.assertIn("data", request.json)
        self.assertIn("message", request.json)
        self.assertEqual(False, request.json["success"])
        self.assertDictEqual(request.json["data"], {})

    def test_token_expired(self):
        request = self.app.get("/api/token/refresh", headers={"Authorization": expired_token})
        self.assertEqual(401, request.status_code)
        self.assertIn("success", request.json)
        self.assertIn("data", request.json)
        self.assertIn("message", request.json)
        self.assertEqual(False, request.json["success"])
        self.assertDictEqual(request.json["data"], {})
    
    @patch.dict(os.environ, {"JWT_SECRET": "production_jwt_secret"})
    def test_jwt_from_env(self):
        self.assertEqual(get_jwt_secret(), "production_jwt_secret")

    @patch.dict(os.environ, {})
    def test_jwt_not_from_env(self):
        self.assertEqual(get_jwt_secret(), DEFAULT_JWT_SECRET)
