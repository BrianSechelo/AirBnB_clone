#!/usr/bin/python3
"""
Module for the user class
"""

from models.base_model import BaseModel

class User(BaseModel):
    """
    class User that handles user's information"
    """
    emai = ""
    password = ""
    first_name = ""
    last_name = ""
