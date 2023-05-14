#!/usr/bin/python3
"""This is a module that creates a Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """A Class for managing review objects"""

    place_id = ""
    user_id = ""
    text = ""
