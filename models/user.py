#!/usr/bin/python3
""" User class"""


class User(BaseModel):
    """ class User that inherits from BaseModel"""
    """ Task 8 """
    def __init__(self):
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
