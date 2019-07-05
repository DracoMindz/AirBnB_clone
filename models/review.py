#!/usr/bin/python3
"""Review class"""
"""task 9"""

from models.base_model import BaseModel



class Review(BaseModel):
    """ inherit from base. has public class attributes"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ init review """
        super.__init__(*args, **kwargs)
