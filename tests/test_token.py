import unittest
from unittest.mock import patch

from routes import app as test_app

from .model import MOCKED_JWT_SECRET, valid_token


@patch("utils.auth.JWT_SECRET", MOCKED_JWT_SECRET)
class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = test_app.test_client()

    @patch("utils.auth.JWT_SECRET", MOCKED_JWT_SECRET)
    def test_token_refresh_success(self):
        request = self.app.get("/api/token/refresh", headers={"Authorization": valid_token})
        self.assertEqual(request.status_code, 200)
        self.assertIn("success", request.json)
        self.assertIn("data", request.json)
        self.assertIn("message", request.json)
        self.assertEqual(True, request.json["success"])
        self.assertIn("token", request.json["data"])
        self.assertIsNotNone(request.json["data"]["token"])
