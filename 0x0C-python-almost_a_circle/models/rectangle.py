#!/usr/bin/python3
"""Class Rectangle a child of Base class"""

from models.base import Base


class Rectangle(Base):
    """Represents a rectangle

    Inherits from: Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a rectangle
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """retrieve width property"""

        return self.__width

    @width.setter
    def width(self, value):
        """sets the width value"""

        self.setter_validation("width", value)
        self.__width = value

    @property
    def height(self):
        """retrieves height property"""

        return self.__height

    @height.setter
    def height(self, value):
        """sets the width property"""

        self.setter_validation("height", value)
        self.__height = value

    @property
    def x(self):
        """Retrieves property x"""

        return self.__x

    @x.setter
    def x(self, value):
        """sets the x property"""

        self.setter_validation("x", value)
        self.__x = value

    @property
    def y(self):
        """Returns private attribute"""

        return self.__y

    @y.setter
    def y(self, value):
        """sets the private attribute"""
        self.setter_validation("y", value)
        self.__y = value

    @staticmethod
    def setter_validation(attribute, value):
        """Validates value of an attribute before its set"""

        if not isinstance(value, int):
            raise TypeError(f"{attribute} must be an integer")
        elif attribute == "x" or attribute == "y":
            if value < 0:
                raise ValueError(f"{attribute} must be >= 0")
        elif value <= 0:
            raise ValueError(f"{attribute} must be > 0")
