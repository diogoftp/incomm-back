import unittest
from unittest.mock import patch

import mongomock
from routes import app as test_app
from utils.database import database

from .model import MOCKED_JWT_SECRET, card_object, valid_token


@patch("utils.auth.JWT_SECRET", MOCKED_JWT_SECRET)
class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = test_app.test_client()
        self.db = mongomock.MongoClient()["GiftCards"]
        self.db.gift_cards.insert_one(card_object)

    def test_info_not_logged_in(self):
        request = self.app.get("/api/info")
        self.assertEqual(401, request.status_code)
        self.assertIn("success", request.json)
        self.assertIn("data", request.json)
        self.assertIn("message", request.json)
        self.assertEqual(False, request.json["success"])
        self.assertNotIn("card_data", request.json["data"])

    def test_info_success(self):
        with patch.object(database, "gift_cards", new=self.db.gift_cards):
            request = self.app.get("/api/info", headers={"Authorization": valid_token})
            self.assertEqual(request.status_code, 200)
            self.assertIn("success", request.json)
            self.assertIn("data", request.json)
            self.assertIn("message", request.json)
            self.assertEqual(True, request.json["success"])
            self.assertIn("card_data", request.json["data"])
            self.assertIsNotNone(request.json["data"]["card_data"])

    def test_info_invalid_card(self):
        with patch.object(database, "gift_cards", new=self.db.gift_cards):
            self.db.gift_cards.delete_one({"number": card_object["number"]})
            request = self.app.get("/api/info", headers={"Authorization": valid_token})
            self.assertEqual(request.status_code, 200)
            self.assertIn("success", request.json)
            self.assertIn("data", request.json)
            self.assertIn("message", request.json)
            self.assertEqual(False, request.json["success"])
            self.assertIn("card_data", request.json["data"])
            self.assertIsNone(request.json["data"]["card_data"])
