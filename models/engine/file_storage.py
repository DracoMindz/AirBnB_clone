#!/usr/bin/python3
"""File Storage Class"""
""" task 5"""

import json
from models.base_model import BaseModel
import uuid
from datetime import datetime

class FileStorage:
    """public instance attrs for FileStorage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        for key, value in FileStorage.__objects.items():
            if not isinstance(value, dict):
                FileStorage.__objects[key] = value.to_dict()
            with open(FileStorage.__file_path, "w") as write_file:
                json.dump(FileStorage.__objects, write_file)

    def reload(self):
        import os.path
        from models.base_model import BaseModel
        from models.user import User



        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as my_file:
                FileStorage.__objects = json.load(my_file)
        for key, value in FileStorage.__objects.items():
            if 'BaseModel' in key:
                new_obj = BaseModel(None, **value)
            elif 'User' in key:
                new_obj = User(None, **value)
            FileStorage.__objects[key] = new_obj
