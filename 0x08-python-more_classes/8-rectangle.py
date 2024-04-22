#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """Represents a rectangle
    Attributes:
        number_of_instances (int): Number of rectangle instances
        print_symbol (any): symbol used for string representation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a rectangle
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
        symbol = str(self.print_symbol)
        for h in range(self.__height):
            [rect.append(symbol) for w in range(self.__width)]
            if h != self.__height - 1:
                rect.append('\n')
        # convert the list to a single printable string using .join()
        return ("".join(rect))

    def __repr__(self):
        """Returns a string representation of the rectangle"""

        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message when an instance of a rectangle is deleted"""

        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based of the area"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 < area_2:
            return (rect_2)
        else:
            return (rect_1)
