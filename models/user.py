#!/usr/bin/python3
"""This is a module that creates a User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """A Class for managing user objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
