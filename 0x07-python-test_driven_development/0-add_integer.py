#!/usr/bin/python3
"""Defines an integer addition function"""


def add_integer(a, b=98):
    """
    Returns the integer addition of a and b.

    Floats arguments are typecasted to to int before addition
    Raises:
        TypeError: if either a or b is a either a non-integer or non-float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
