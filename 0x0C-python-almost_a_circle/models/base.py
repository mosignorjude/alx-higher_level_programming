#!/usr/bin/python3
"""Defines the base class for other instances"""


class Base:
    """Represents the base model.
    Represents the "base" for all other classes in this project
    Attributes:
        __nb_objects (int): The number of instantiated Base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new Base.
        Args:
            id (int): The identity of the new Base
        """

        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
