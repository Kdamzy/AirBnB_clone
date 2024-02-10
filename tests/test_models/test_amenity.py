#!/usr/bin/python3
"""Unittests for amenity.py"""
import unittest
from datetime import datetime
from models.amenity import Amenity
import os


class TestAmenity(unittest.TestCase):
    """Unittests for the Amenity class"""
    def test_instance_creation(self):
        """Test creation of Amenity instance."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        
    def test_attribute_default_values(self):
        """Test default values of Amenity attributes."""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
        
    def test_attribute_assignment(self):
        """Test assignment of Amenity attributes."""
        amenity = Amenity()
        amenity.name = "kenny"
        self.assertEqual(amenity.name, "Wifi")

    def test_to_dict_method(self):
        """Test to_dict method of Amenity."""
        amenity = Amenity()
        amenity_dict = amenity.to_dict()

        self.assertIsInstance(amenity_dict, dict)
        self.assertIn('__class__', amenity_dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')

        self.assertIn('name', amenity_dict)
        self.assertEqual(amenity_dict['name'], amenity.name)

    def test_from_dict_method(self):
        """Test from_dict method of Amenity."""
        amenity_data = {
            '__class__': 'Amenity',
            'id': '123',
            'name': 'kenny',
            'created_at': '2022-01-01T00:00:00.000000',
            'updated_at': '2022-01-01T00:00:00.000000'
        }
        amenity = Amenity()
        amenity.from_dict(amenity_data)

        self.assertEqual(amenity.id, '123')
        self.assertEqual(amenity.name, 'Swimming Pool')
        self.assertEqual(amenity.created_at,
                         datetime.strptime(amenity_data['created_at'], "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(amenity.updated_at,
                         datetime.strptime(amenity_data['updated_at'], "%Y-%m-%dT%H:%M:%S.%f"))

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        amenity = Amenity()
        first_updated_at = amenity.updated_at
        amenity.save()
        self.assertLess(first_updated_at, amenity.updated_at)

    def test_two_saves(self):
        amenity = Amenity()
        first_updated_at = amenity.updated_at
        amenity.save()
        second_updated_at = amenity.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        amenity.save()
        self.assertLess(second_updated_at, amenity.updated_at)

    def test_save_with_arg(self):
        amenity = Amenity()
        with self.assertRaises(TypeError):
            amenity.save(None)

    def test_save_updates_file(self):
        amenity = Amenity()
        amenity.save()
        amenity_id = "Amenity." + amenity.id
        with open("file.json", "r") as f:
            self.assertIn(amenity_id, f.read())

if __name__ == "__main__":
    unittest.main()
