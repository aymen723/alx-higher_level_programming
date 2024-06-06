#!/usr/bin/python3
"""rectengle class inherent from basegeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rept rectangle."""

    def __init__(self, width, height):
        """contructer a new Rectangle.

        Args:
            width (int): The width.
            height (int): The height.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
