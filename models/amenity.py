#!/usr/bin/python3
"""Lists the Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Reps an amenity.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
