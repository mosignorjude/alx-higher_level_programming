#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a Square"""

    @property
    def size(self):
        """retrieve size property"""
        return self.__size

    @property
    def position(self):
        """retrieve the position property"""
        return self.__position

    @size.setter
    def size(self, value):
        """sets the size property"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """sets the position property"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
            position (int, int): position of the new square
        """
        self.size = size
        self.position = position

    def area(self):
        """Calculates the area of the square.

        Returns: The area of the square.
        """
        return (self.__size * self.__size)

    def my_print(self):
        """Prints a square using #."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
