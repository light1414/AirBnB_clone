#!/usr/bin/python3
"""Lists the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Reps a state.

    Attributes:
        name (str): The name of the state.
    """

    name = ""
