#!/usr/bin/python3
""" User class"""
from models.base_model import BaseModel

class User(BaseModel):
    """ class User that inherits from BaseModel"""
    """ Task 8 """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ init user """
        super().__init__(*args, **kwargs)
