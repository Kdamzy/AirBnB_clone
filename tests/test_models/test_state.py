#!/usr/bin/python3
"""Unittests for state.py"""
import unittest
import os
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):
    """Unittests for the State class."""

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
        """Test creation of State instance."""
        state = State()
        self.assertIsInstance(state, State)

    def test_attribute_default_values(self):
        """Test default values of State attributes."""
        state = State()
        self.assertEqual(state.name, "")

    def test_attribute_assignment(self):
        """Test assignment of State attributes."""
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")

    def test_to_dict_method(self):
        """Test to_dict method of State."""
        state = State()
        state_dict = state.to_dict()

        self.assertIsInstance(state_dict, dict)
        self.assertIn('__class__', state_dict)
        self.assertEqual(state_dict['__class__'], 'State')

        self.assertIn('name', state_dict)
        self.assertEqual(state_dict['name'], state.name)

    def test_from_dict_method(self):
        """Test from_dict method of State."""
        state_data = {
            '__class__': 'State',
            'id': '123',
            'name': 'California',
            'created_at': '2022-01-01T00:00:00.000000',
            'updated_at': '2022-01-01T00:00:00.000000'
        }
        state = State()
        state.from_dict(state_data)

        self.assertEqual(state.id, '123')
        self.assertEqual(state.name, 'California')


if __name__ == '__main__':
    unittest.main()
