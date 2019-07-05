#!/usr/bin/python3
""" User class"""
from models.base_model import BaseModel

class User(BaseModel):
    """ class User that inherits from BaseModel"""
    """ Task 8 """
    def __init__(self):
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
