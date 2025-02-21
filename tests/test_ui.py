import unittest
import streamlit as st
from streamlit.testing.v1 import AppTest

class TestUI(unittest.TestCase):
    def test_app_load(self):
        """Check if the Streamlit app loads without errors."""
        app = AppTest("frontend/app.py")
        app.run()
        self.assertFalse(app.exception, "Streamlit app crashed!")

    def test_login_form(self):
        """Check if login form elements exist."""
        app = AppTest("frontend/app.py")
        app.run()
        assert app.text_input("Username"), "Username input field missing!"
        assert app.text_input("Password"), "Password input field missing!"

if __name__ == '__main__':
    unittest.main()
