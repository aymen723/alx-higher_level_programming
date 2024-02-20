#!/usr/bin/python3
"""class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check an object is the same class.

    Args:
        obj (any): obj.
        a_class (type): class to check.
    Returns:
        true or false.
    """
    if isinstance(obj, a_class):
        return True
    return False
