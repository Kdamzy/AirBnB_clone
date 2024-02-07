#!/usr/bin/python3
"""__init__ method for models directory"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
"""reload back to dictionary from json format"""
storage.reload()
