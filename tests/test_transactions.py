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

    def mocked_requests_get(*args, **kwargs):
        class MockRequestsResponse:
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code
        return MockRequestsResponse(None, 404)

    def test_transactions_internal_not_logged_in(self):
        request = self.app.get("/api/transactions")
        self.assertEqual(401, request.status_code)
        self.assertIn("success", request.json)
        self.assertIn("data", request.json)
        self.assertIn("message", request.json)
        self.assertEqual(False, request.json["success"])
        self.assertDictEqual(request.json["data"], {})

    def test_transactions_internal_success(self):
        with patch.object(database, "gift_cards", new=self.db.gift_cards):
            request = self.app.get("/api/transactions", headers={"Authorization": valid_token})
            self.assertEqual(request.status_code, 200)
            self.assertIn("success", request.json)
            self.assertIn("data", request.json)
            self.assertIn("message", request.json)
            self.assertEqual(True, request.json["success"])
            self.assertIn("transactions_data", request.json["data"])
            self.assertIsNotNone(request.json["data"]["transactions_data"])

    def test_transactions_external_not_logged_in(self):
        request = self.app.get("/api/transactions/external")
        self.assertEqual(401, request.status_code)
        self.assertIn("success", request.json)
        self.assertIn("data", request.json)
        self.assertIn("message", request.json)
        self.assertEqual(False, request.json["success"])
        self.assertDictEqual(request.json["data"], {})

    def test_transactions_external_success(self):
        with patch.object(database, "gift_cards", new=self.db.gift_cards):
            request = self.app.get("/api/transactions/external", headers={"Authorization": valid_token})
            self.assertEqual(request.status_code, 200)
            self.assertIn("success", request.json)
            self.assertIn("data", request.json)
            self.assertIn("message", request.json)
            self.assertEqual(True, request.json["success"])
            self.assertIn("transactions_data", request.json["data"])
            self.assertIsNotNone(request.json["data"]["transactions_data"])

    @patch("requests.get", side_effect=mocked_requests_get)
    def test_transactions_external_fail(self, mocked_get):
        with patch.object(database, "gift_cards", new=self.db.gift_cards):
            request = self.app.get("/api/transactions/external", headers={"Authorization": valid_token})
            self.assertEqual(request.status_code, 200)
            self.assertIn("success", request.json)
            self.assertIn("data", request.json)
            self.assertIn("message", request.json)
            self.assertEqual(False, request.json["success"])
            self.assertIn("transactions_data", request.json["data"])
            self.assertIsNone(request.json["data"]["transactions_data"])
