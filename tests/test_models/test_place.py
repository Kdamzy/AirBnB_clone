#!/usr/bin/python3
"""unittests for place.py"""
import unittest
from models.place import Place
from datetime import datetime
import os


class TestPlace(unittest.TestCase):
    """Unittests for the Place class."""

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
        """Test creation of Place instance."""
        place = Place()
        self.assertIsInstance(place, Place)

    def test_attribute_default_values(self):
        """Test default values of Place attributes."""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_attribute_assignment(self):
        """Test assignment of Place attributes."""
        place = Place()
        place.city_id = "123"
        place.user_id = "456"
        place.name = "luton"
        place.description = "cardigan street"
        place.number_rooms = 3
        place.number_bathrooms = 2
        place.max_guest = 6
        place.price_by_night = 100
        place.latitude = 45.678
        place.longitude = -123.456
        place.amenity_ids = ["789", "012"]
        self.assertEqual(place.city_id, "123")
        self.assertEqual(place.user_id, "456")
        self.assertEqual(place.name, "luton")
        self.assertEqual(place.description, "cardigan street")
        self.assertEqual(place.number_rooms, 3)
        self.assertEqual(place.number_bathrooms, 2)
        self.assertEqual(place.max_guest, 6)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 45.678)
        self.assertEqual(place.longitude, -123.456)
        self.assertEqual(place.amenity_ids, ["789", "012"])

    def test_to_dict_method(self):
        """Test to_dict method of Place."""
        place = Place()
        place_dict = place.to_dict()

        self.assertIsInstance(place_dict, dict)
        self.assertIn('__class__', place_dict)
        self.assertEqual(place_dict['__class__'], 'Place')

        self.assertIn('city_id', place_dict)
        self.assertEqual(place_dict['city_id'], place.city_id)

        self.assertIn('user_id', place_dict)
        self.assertEqual(place_dict['user_id'], place.user_id)

        self.assertIn('name', place_dict)
        self.assertEqual(place_dict['name'], place.name)

        self.assertIn('description', place_dict)
        self.assertEqual(place_dict['description'], place.description)

        self.assertIn('number_rooms', place_dict)
        self.assertEqual(place_dict['number_rooms'], place.number_rooms)

        self.assertIn('number_bathrooms', place_dict)
        self.assertEqual(place_dict['number_bathrooms'], place.number_bathrooms)

        self.assertIn('max_guest', place_dict)
        self.assertEqual(place_dict['max_guest'], place.max_guest)

        self.assertIn('price_by_night', place_dict)
        self.assertEqual(place_dict['price_by_night'], place.price_by_night)

        self.assertIn('latitude', place_dict)
        self.assertEqual(place_dict['latitude'], place.latitude)

        self.assertIn('longitude', place_dict)
        self.assertEqual(place_dict['longitude'], place.longitude)

        self.assertIn('amenity_ids', place_dict)
        self.assertEqual(place_dict['amenity_ids'], place.amenity_ids)

    def test_from_dict_method(self):
        """Test from_dict method of Place."""
        place_data = {
            '__class__': 'Place',
            'id': '123',
            'city_id': '456',
            'user_id': '789',
            'name': 'Cozy Cabin',
            'description': 'A beautiful cabin in the woods',
            'number_rooms': 3,
            'number_bathrooms': 2,
            'max_guest': 6,
            'price_by_night': 100,
            'latitude': 45.678,
            'longitude': -123.456,
            'amenity_ids': ['012', '345'],
            'created_at': '2022-01-01T00:00:00.000000',
            'updated_at': '2022-01-01T00:00:00.000000'
        }
        place = Place()
        place.from_dict(place_data)

        self.assertEqual(place.id, '123')
        self.assertEqual(place.city_id, '456')
        self.assertEqual(place.user_id, '789')
        self.assertEqual(place.name, 'luton')
        self.assertEqual(place.description, 'cardigan street')
        self.assertEqual(place.number_rooms, 3)
        self

if __name__ == "__main__":
    unittest.main()
