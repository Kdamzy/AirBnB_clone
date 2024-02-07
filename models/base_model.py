#!/usr/bin/python3
"""create a BaseModel class"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseModel for the HBnB project"""

    def __init__(self, *args, **kwargs):
        """initialization of the basemodel instances"""
        
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            dates_format = "%Y-%m-%dT%H:%M:%S.%f"
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.strptime(v, dates_format))
                else:
                    setattr(self, k, v)
        else:
            models.storage.new(self)

    def save(self):
        """Update updated_at with the present datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance"""
        dict_copy = dict(self.__dict__)
        dict_copy["updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dict_copy["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dict_copy["__class__"] = self.__class__.__name__
        return (dict_copy)

    def __str__(self):
        """Return the str representation of the BaseModel instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
