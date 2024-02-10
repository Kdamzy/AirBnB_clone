#!/usr/bin/python3
"""Unittests for user.py"""
import unittest
import os
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    """Unittests for the User class."""

    @classmethod
    def setUpClass(cls):
        """Create file.json if it doesn't exist."""
        try:
            with open("file.json", "x") as f:
                f.write("{}")
        except FileExistsError:
            pass

    @classmethod
    def tearDownClass(cls):
        """Delete file.json."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instance_creation(self):
        """Test creation of User instance."""
        user = User()
        self.assertIsInstance(user, User)

    def test_attribute_default_values(self):
        """Test default values of User attributes."""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_attribute_assignment(self):
        """Test assignment of User attributes."""
        user = User()
        user.email = "test@kenny.com"
        user.password = "password123"
        user.first_name = "kenny"
        user.last_name = "presh"
        self.assertEqual(user.email, "test@kenny.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "kenny")
        self.assertEqual(user.last_name, "presh")

    def test_to_dict_method(self):
        """Test to_dict method of User."""
        user = User()
        user_dict = user.to_dict()

        self.assertIsInstance(user_dict, dict)
        self.assertIn('__class__', user_dict)
        self.assertEqual(user_dict['__class__'], 'User')

        self.assertIn('email', user_dict)
        self.assertEqual(user_dict['email'], user.email)

        self.assertIn('password', user_dict)
        self.assertEqual(user_dict['password'], user.password)

        self.assertIn('first_name', user_dict)
        self.assertEqual(user_dict['first_name'], user.first_name)

        self.assertIn('last_name', user_dict)
        self.assertEqual(user_dict['last_name'], user.last_name)

    def test_from_dict_method(self):
        """Test from_dict method of User."""
        user_data = {
            '__class__': 'User',
            'id': '123',
            'email': 'test@kenny.com',
            'password': 'password123',
            'first_name': 'kenny',
            'last_name': 'presh',
            'created_at': '2022-01-01T00:00:00.000000',
            'updated_at': '2022-01-01T00:00:00.000000'
        }
        user = User()
        user.from_dict(user_data)

        self.assertEqual(user.id, '123')
        self.assertEqual(user.email, 'test@kenny.com')
        self.assertEqual(user.password, 'password123')
        self.assertEqual(user.first_name, 'kenny')
        self.assertEqual(user.last_name, 'presh')


if __name__ == '__main__':
    unittest.main()
