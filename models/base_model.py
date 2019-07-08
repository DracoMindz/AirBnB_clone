#!/usr/bin/python3
""" Base Model HELLO"""

import models
import json
import uuid
from datetime import datetime

timeFormat = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    """ public instance attrs for BaseModel go here """
    def __init__(self, **kwargs):
        """ initializes a new instance of BaseModel """

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at"or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, timeFormat))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """ returns a string representtation of the BaseModel instance """
        className = self.__class__.__name__
        return "[{}] ({}) {}".format(className, self.id, self.__dict__)

    def save(self):
        """ updates the instance updated_at attr with current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dict containing key/values of instances dict """
        this_dict = self.__dict__.copy()
        this_dict.update({"__class__": "{}".format(self.__class__.__name__)})
        if this_dict["created_at"] is not None:
            this_dict["created_at"] = datetime.isoformat((self.created_at))
        if this_dict["updated_at"] is not None:
            this_dict["updated_at"] = datetime.isoformat((self.updated_at))
        return this_dict
