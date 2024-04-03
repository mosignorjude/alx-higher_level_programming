#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a Square"""

    @property
    def size(self):
        """retrieve size property"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size property"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        self.__size = size

    def area(self):
        """Calculates the area of the square.

        Returns: The area of the square.
        """
        return (self.__size * self.__size)

    def my_print(self):
        """Prints a square using #."""

        len = self.__size
        width = len

        if self.__size == 0:
            print()
        for i in range(len):
            for j in range(width):
                print("#", end="")
            print()
