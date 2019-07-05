#!/usr/bin/python3
"""Amenity class"""
"""task 9"""

from models.base_model import BaseModel

class Amenity(BaseModel):
    """inhereits BaseModel has public attributes"""
    name = ""

    def __init__(self, *args, **kwargs):
        """ init amenity """
        super().__init__(*args, **kwargs)
