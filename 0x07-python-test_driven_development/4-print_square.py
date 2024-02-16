#!/usr/bin/python3
"""a function to print a square"""


def print_square(size):
    """func to a square with #.

    Args:
        size (int): height and width.
    Raises:
        TypeError: if size is not integer.
        ValueError: size < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
