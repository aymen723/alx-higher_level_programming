#!/usr/bin/python3
"""a integer add function."""


def add_integer(a, b=98):
    """Retr the add of integer of a and b.

    if flaot argument is passed it will be typedcast into integer.

    Raises:
        TypeError: if etiher a or b are not integer or float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
