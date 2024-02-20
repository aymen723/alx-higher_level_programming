#!/usr/bin/python3
"""function to class-checking."""


def inherits_from(obj, a_class):
    """Check an object is the same class.

    Args:
        obj (any): obj.
        a_class (type): class to check.
    Returns:
        true or false.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
