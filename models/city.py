#!/usr/bin/python3
""" City class"""
""" task 9"""
from models.base_model import BaseModel



class City(BaseModel):
    """ my parent is BaseModel """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ init city """
        super().__init__(*args, **kwargs)
