#!/usr/bin/python3
"""rectengle class inherent from basegeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rept rectangle."""

    def __init__(self, width, height):
        """contructer for Rectangle.

        Args:
            width (int): The width.
            height (int): The height.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """area of rectang."""
        return self.__width * self.__height

    def __str__(self):
        """Return rept for a rect."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
