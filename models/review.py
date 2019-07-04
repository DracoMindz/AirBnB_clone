#!/usr/bin/python3
"""Review class"""
"""task 9"""


class Review(BaseModel):
    """ inherit from base. has public class attributes"""
    def __init__(self):
        self.place_id = ""
        self.user_id = ""
        self.text = ""
