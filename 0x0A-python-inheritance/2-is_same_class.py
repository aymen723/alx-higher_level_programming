#!/usr/bin/python3
"""a function to check a class."""


def is_same_class(obj, a_class):
    """Check an object is the same class.

    Args:
        obj (any): obj.
        a_class (type): class to check.
    Returns:
        true or false.
    """
    if type(obj) == a_class:
        return True
    return False
