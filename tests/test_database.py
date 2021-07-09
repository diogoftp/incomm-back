import os
import unittest
from unittest.mock import patch

import mongomock
from routes import app as test_app
from utils.database import (DEFAULT_DB_NAME, DEFAULT_DB_URI, get_db_name,
                            get_db_uri)

from tests.model import MOCKED_JWT_SECRET


@patch("utils.auth.JWT_SECRET", MOCKED_JWT_SECRET)
class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = test_app.test_client()
        self.db = mongomock.MongoClient()["GiftCards"]

    @patch.dict(os.environ, {"DB_URI": "production_db_uri", "DB_NAME": "production_db_name"})
    def test_database_from_env(self):
        self.assertEqual(get_db_uri(), "production_db_uri")
        self.assertEqual(get_db_name(), "production_db_name")

    @patch.dict(os.environ, {})
    def test_database_not_from_env(self):
        self.assertEqual(get_db_uri(), DEFAULT_DB_URI)
        self.assertEqual(get_db_name(), DEFAULT_DB_NAME)
