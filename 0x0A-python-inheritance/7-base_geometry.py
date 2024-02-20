#!/usr/bin/python3
"""class BaseGeometry."""


class BaseGeometry:
    """rep base geometry."""

    def area(self):
        """not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """verfie the params as integer.

        Args:
            name (str): name.
            value (int): param.
        Raises:
            TypeError: If value not an integer.
            ValueError: value <0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
