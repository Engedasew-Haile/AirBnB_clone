#!/usr/bin/python3

"""
define user class
"""

class User(BaseModel):
  """Rep a user
  
   Attributes:
        email (str): user email
        password (str): user password
        first_name (str): first name
        last_name (str): last name

    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
