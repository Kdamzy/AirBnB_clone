#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent an abstracted storage engine."""
    __objects = {}
    __file_path = "file.json"

    def all(self):
        """Return the dictionary objects."""
        return self.__objects

    def new(self, obj):
        """Set the new objects into __object with key"""
        obj_key = obj.__class__.__name__
        self.__objects["{}.{}".format(obj_key, obj.id)] = obj

    def save(self):
        """retrieve all objects into JSON file"""     
        dict_obj = {}
        for key, val in self.__objects.items():
            dict_obj[key] = val.to_dict()

        with open(self.__file_path, mode='w', encoding="UTF8") as fd:
            json.dump(dict_obj, fd)

    def reload(self):
        """Deserialize the JSON file."""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                dict_obj = json.load(f)
                for item in dict_obj.values():
                    cls_name = item["__class__"]
                    del item["__class__"]
                    self.new(eval(cls_name)(**item))
        except FileNotFoundError:
            return
 