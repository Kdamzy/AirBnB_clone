#!/usr/bin/python3
"""Unittests for review.py"""
import unittest
import os
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):
    """Unittests for the Review class."""

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
        """Test creation of Review instance."""
        review = Review()
        self.assertIsInstance(review, Review)

    def test_attribute_default_values(self):
        """Test default values of Review attributes."""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_attribute_assignment(self):
        """Test assignment of Review attributes."""
        review = Review()
        review.place_id = "123"
        review.user_id = "456"
        review.text = "Great experience!"
        self.assertEqual(review.place_id, "123")
        self.assertEqual(review.user_id, "456")
        self.assertEqual(review.text, "Great experience!")

    def test_to_dict_method(self):
        """Test to_dict method of Review."""
        review = Review()
        review_dict = review.to_dict()

        self.assertIsInstance(review_dict, dict)
        self.assertIn('__class__', review_dict)
        self.assertEqual(review_dict['__class__'], 'Review')

        self.assertIn('place_id', review_dict)
        self.assertEqual(review_dict['place_id'], review.place_id)

        self.assertIn('user_id', review_dict)
        self.assertEqual(review_dict['user_id'], review.user_id)

        self.assertIn('text', review_dict)
        self.assertEqual(review_dict['text'], review.text)

    def test_from_dict_method(self):
        """Test from_dict method of Review."""
        review_data = {
            '__class__': 'Review',
            'id': '123',
            'place_id': '456',
            'user_id': '789',
            'text': 'Great experience!',
            'created_at': '2022-01-01T00:00:00.000000',
            'updated_at': '2022-01-01T00:00:00.000000'
        }
        review = Review()
        review.from_dict(review_data)

        self.assertEqual(review.id, '123')
        self.assertEqual(review.place_id, '456')
        self.assertEqual(review.user_id, '789')
        self.assertEqual(review.text, 'Great experience!')


if __name__ == '__main__':
    unittest.main()
