#!/usr/bin/python3
"""module for FileStorage class"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BaseModel,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """class to store and return obejects using JSON"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the objects dictionary"""
        return self.__objects

    def new(self, obj):
        """creates dictionary of object"""
        if obj is not None:
            key = '{}.{}'.format(type(obj).__name__, obj.id)
            self.__objects[key] = obj


    def reload(self):
        """deserializes the JSON file to __objects
        if the file exists, do nothing otherwise"""
        try:
            with open(FileStorage.__file_path, mode="r",
                      encoding="UTF-8") as to_file:
                obj_load = json.load(to_file)
                from models.base_model import BaseModel
                from models.amenity import Amenity
                from models.place import Place
                from models.review import Review
                from models.state import State
                from models.user import User

                class_list = ["BaseModel", "Amenity", "City", "Place",
                              "Review", "State", "User"]
                for key, value in obj_load.items():
                    if value.get("__class__") in class_list:
                        method = value.get("__class__")
                        self.__objects[key] = eval(
                            str(method))(obj_load[key])
        except:
            pass

    def save(self):
        """save to JSON storage file"""
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, mode="w",
                  encoding="UTF-8") as to_file:
            json.dump(new_dict, to_file)
