#!/usr/bin/python3
""" City class"""
""" task 9"""


class City(BaseModel):
    """ my parent is BaseModel """
    def __init__(self):
        self.state_id = ""
        self.name = ""
