#!/usr/bin/python3
"""Unittest for city.py"""
import unittest
from models.city import City
from datetime import datetime
import os

class TestCity(unittest.TestCase):
    """Unittests for the City class."""

    def test_instance_creation(self):
        """Test creation of City instance."""
        city = City()
        self.assertIsInstance(city, City)

    def test_attribute_default_values(self):
        """Test default values of City attributes."""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_attribute_assignment(self):
        """Test assignment of City attributes."""
        city = City()
        city.state_id = "UK"
        city.name = "United Kingdom"
        self.assertEqual(city.state_id, "UK")
        self.assertEqual(city.name, "United Kingdom")

    def test_to_dict_method(self):
        """Test to_dict method of City."""
        city = City()
        city_dict = city.to_dict()

        self.assertIsInstance(city_dict, dict)
        self.assertIn('__class__', city_dict)
        self.assertEqual(city_dict['__class__'], 'City')

        self.assertIn('state_id', city_dict)
        self.assertEqual(city_dict['state_id'], city.state_id)

        self.assertIn('name', city_dict)
        self.assertEqual(city_dict['name'], city.name)

    def test_from_dict_method(self):
        """Test from_dict method of City."""
        city_data = {
            '__class__': 'City',
            'id': '123',
            'state_id': 'UK',
            'name': 'United Kingdom',
            'created_at': '2022-01-01T00:00:00.000000',
            'updated_at': '2022-01-01T00:00:00.000000'
        }
        city = City()
        city.from_dict(city_data)

        self.assertEqual(city.id, '123')
        self.assertEqual(city.state_id, 'UK')
        self.assertEqual(city.name, 'United Kingdom')
        self.assertEqual(city.created_at,
                         datetime.strptime(city_data['created_at'], "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(city.updated_at,
                         datetime.strptime(city_data['updated_at'], "%Y-%m-%dT%H:%M:%S.%f"))

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        city = City()
        first_updated_at = city.updated_at
        city.save()
        self.assertLess(first_updated_at, city.updated_at)

    def test_two_saves(self):
        city = City()
        first_updated_at = city.updated_at
        city.save()
        second_updated_at = city.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        city.save()
        self.assertLess(second_updated_at, city.updated_at)

    def test_save_with_arg(self):
        city = City()
        with self.assertRaises(TypeError):
            city.save(None)

    def test_save_updates_file(self):
        city = City()
        city.save()
        city_id = "City." + city.id
        with open("file.json", "r") as f:
            self.assertIn(city_id, f.read())


if __name__ == "__main__":
    unittest.main()
