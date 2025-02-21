import unittest
import sqlite3
from backend.db import init_db, add_transaction, get_transactions
from backend.auth import register_user, authenticate_user

class TestDatabase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Initialize database before running tests."""
        init_db()

    def test_register_user(self):
        """Test user registration."""
        success = register_user("test_user", "password123")
        self.assertTrue(success, "User registration failed.")

    def test_authenticate_user(self):
        """Test user authentication."""
        register_user("test_login", "test123")
        is_authenticated = authenticate_user("test_login", "test123")
        self.assertTrue(is_authenticated, "User authentication failed.")

    def test_add_transaction(self):
        """Test adding a new transaction."""
        user_id = 1  # Test user ID
        add_transaction(user_id, "2025-02-21", "Food", "Expense", 500, "Lunch")
        transactions = get_transactions(user_id)
        self.assertGreater(len(transactions), 0, "Transaction was not added.")

if __name__ == '__main__':
    unittest.main()
