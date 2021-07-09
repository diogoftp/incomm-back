import unittest
from unittest.mock import patch

import mongomock
from routes import app as test_app
from utils.database import database

from .model import MOCKED_JWT_SECRET, card_object


@patch("utils.auth.JWT_SECRET", MOCKED_JWT_SECRET)
class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = test_app.test_client()
        self.db = mongomock.MongoClient()["GiftCards"]
        self.db.gift_cards.insert_one(card_object)

    def test_login_empty_body(self):
        request = self.app.post("/api/login")
        self.assertEqual(400, request.status_code)

    def test_login_success(self):
        with patch.object(database, "gift_cards", new=self.db.gift_cards):
            request = self.app.post("/api/login", data={"card_number": "1111111111111111", "password": "123456"})
            self.assertEqual(request.status_code, 200)
            self.assertIn("success", request.json)
            self.assertIn("data", request.json)
            self.assertIn("message", request.json)
            self.assertEqual(True, request.json["success"])
            self.assertIn("token", request.json["data"])
            self.assertIsNotNone(request.json["data"]["token"])
    
    def test_login_wrong_card(self):
        with patch.object(database, "gift_cards", new=self.db.gift_cards):
            request = self.app.post("/api/login", data={"card_number": "22222222222222222", "password": "123456"})
            self.assertEqual(200, request.status_code)
            self.assertIn("success", request.json)
            self.assertIn("data", request.json)
            self.assertIn("message", request.json)
            self.assertEqual(False, request.json["success"])
            self.assertIn("token", request.json["data"])
            self.assertIsNone(request.json["data"]["token"])

    def test_login_wrong_password(self):
        with patch.object(database, "gift_cards", new=self.db.gift_cards):
            request = self.app.post("/api/login", data={"card_number": "1111111111111111", "password": "654321"})
            self.assertEqual(200, request.status_code)
            self.assertIn("success", request.json)
            self.assertIn("data", request.json)
            self.assertIn("message", request.json)
            self.assertEqual(False, request.json["success"])
            self.assertIn("token", request.json["data"])
            self.assertIsNone(request.json["data"]["token"])
