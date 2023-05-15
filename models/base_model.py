#!/usr/bin/python3
"""
    a class BaseModel that defines all common attributes/methods for other classes
"""


from uuid import uuid4
from datetime import datetime
import models

class BaseModelBaseModel:
    """ base for all the classes in the AirBnb console project

    Public instance attributes:
        -> id: string - assign with an uuid when an instance is created:
        -> uuid.uuid4() to generate unique id
        -> unique id for each BaseModel
        -> created_at: datetime instance is created
        -> update_at: datetime every change
