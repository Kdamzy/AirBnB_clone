#!/usr/bin/python3
"""Unittests for base_model implementation"""

import unittest
import os
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unittests for testing of the BaseModel class."""

    def setup(self):
        """Initializing instance"""
        self.my_model = BaseModel()
        self.my_model.name = "Kehinde"

    def TearDown(self):
        """Remove the instance."""
        del self.my_model

    def test_name_set(self):
        """assert that you can add an attribute."""
        self.assertEqual("Kehinde", self.my_model.name)

    def test_id(self):
        """assert the id type"""
        self.assertEqual(str, type(self.my_model.id))

    def test_id_diff(self):
        """Assert that the ids between two instances are different"""
        first_base = BaseModel()
        second_base= BaseModel()
        self.assertNotEqual(first_base.id, second_base.id)

    def test_created_datetime(self):
        self.assertEqual(datetime, type(self.my_model.created_at))

    def test_updated_datetime(self):
        self.assertEqual(datetime, type(self.my_model).updated_at)

    def test_save_update(self):
        """Checks the update of the instance"""
        prev_update = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(prev_update, self.my_model.updated_at)

    def test_unused_args(self):
        """Assert no none value in base model"""
        nobase = BaseModel(None)
        self.assertNotIn(None, nobase.__dict__.values())

    def test_no_kwargs(self):
        """Assert typrerror when passimg kwargs"""
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)


class TestBaseModel_save(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

    @classmethod
    def setUpclass(self):
        """Rename file.json to tmp"""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDownclass(self):
        """Remove file.json and rename tmp to file.json"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp", "file.json")
        except FileNotFoundError:
            pass

    def test_save(self):
        """Test if save method update the instances"""
        my_mod = BaseModel()
        first_updated = my_mod.updated_at
        my_mod.save()
        self.assertLess(first_updated, my_mod.updated_at)

    def test_with_kwargs(self):
        a = datetime.today()
        for_a = a.strftime("%Y-%m-%dT%H:%M:%S.%f")
        my_mod = BaseModel(id="345", created_at=for_a, updated_at=for_a)
        self.assertEqual(my_mod.id, "345")
        self.assertEqual(my_mod.created_at, a)
        self.assertEqual(my_mod.updated_at, a)

    def test_save_with_arg(self):
        """test if save method with argument"""
        my_mod = BaseModel()
        with self.assertRaises(TypeError):
            my_mod.save(None)

    def test_save_new_file(self):
        """test if save method create a new file"""
        my_mod = BaseModel()
        my_mod.save()
        model_id = "BaseModel." + my_mod.id
        with open("file.json", "r") as f:
            self.assertIn(model_id, f.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class."""

    def test_to_dict_type(self):
        """assert if its return a dictionary"""
        my_mod = BaseModel()
        self.assertIsInstance(my_mod.to_dict(), dict)

    def test_to_dict_correct_key(self):
        my_mod = BaseModel()
        self.assertIn("id", my_mod.to_dict())
        self.assertIn("created_at", my_mod.to_dict())
        self.assertIn("updated_at", my_mod.to_dict())
        self.assertIn("__class__", my_mod.to_dict())

    def test_to_dict_datetime(self):
        my_mod = BaseModel()
        model_dict = my_mod.to_dict()
        self.assertIsInstance(str, type(model_dict["created_at"]))
        self.assertIsInstance(str, type(model_dict["updated_at"]))

    def test_contrast_to_dict(self):
        my_mod = BaseModel()
        self.assertNotEqual(my_mod.to_dict(), my_mod.__dict__)

    def test_to_dict_with_arg(self):
        my_mod = BaseModel()
        with self.assertRaises(TypeError):
            my_mod.to_dict(None)


if __name__ == "__main__":
    unittest.main()
