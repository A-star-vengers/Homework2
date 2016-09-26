#!flask/bin/python

import unittest
from flask_testing import TestCase
from app import app
from app.util import getsalt, createhash
from app.dbmodels import User
from app.db import db, init_db

class AppTest(TestCase):

    Testing = True

    def create_app(self):
        return app

    def setUp(self):
        init_db()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class LoginTest(AppTest):

    def test_login(self):

        response = self.client.post("/login", data = dict(
                        username="test",
                        password="test2"
        ), follow_redirects=True)

        assert "Login successful" not in response.data

class RegisterTest(AppTest):

    def test_register(self):

        response = self.client.post("/register", data=dict(
                        username="test",
                        email="test@gmail.com",
                        password="test",
                        confirm="test"
        ), follow_redirects=True)

        assert "Register POST" in response.data

class RegisterAndLoginTest(AppTest):

    def test_register_and_login(self):

        response = self.client.post("/register", data = dict(
                        username="test",
                        email="test@gmail.com",
                        password="test",
                        confirm="test"
        ), follow_redirects=True)

        assert "Register POST" in response.data

        response = self.client.post("/login", data = dict(
                        username="test",
                        password="test"
        ), follow_redirects=True)

        assert "Login successful" in response.data

if __name__ == "__main__":
    unittest.main()