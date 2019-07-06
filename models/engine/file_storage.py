#!/usr/bin/python3
"""File Storage Class"""
""" task 5"""

import json
import os.path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """public instance attrs for FileStorage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the objects dictionary """
        return FileStorage.__objects

    def new(self, obj):
        """ creates a new dictionary of object """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes the objects dictionary to json and writes to file"""
        this_dict = {}
        for key in FileStorage.__objects:
            this_dict[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, 'wt') as json_file:
            json.dump(this_dict, json_file)

    def reload(self):
        """ deserializes json from file to dictionary """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r+") as json_file:
                obj_load = json.load(json_file)
            for key, value in obj_load.items():
                obj_load[key] = eval(value["__class__"])(**value)
