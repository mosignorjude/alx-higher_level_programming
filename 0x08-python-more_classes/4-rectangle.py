#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes a rectangle
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieve width property"""

        return self.__width

    @width.setter
    def width(self, value):
        """sets the width value"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """retrieves height property"""

        return self.__height

    @height.setter
    def height(self, value):
        """sets the width property"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """computes the area of the rectangle"""

        return self.__width * self.__height

    def perimeter(self):
        """computes the perimeter of the rectangle"""

        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Returns printable representation of the rectangle
        prints the rectangle with the character #
        """

        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for h in range(self.__height):
            [rect.append('#') for w in range(self.__width)]
            if h != self.__height - 1:
                rect.append('\n')
        # convert the list to a single printable string using .join()
        return ("".join(rect))

    def __repr__(self):
        """Returns a string representation of the rectangle"""

        return f"Rectangle({self.__width}, {self.__height})"
