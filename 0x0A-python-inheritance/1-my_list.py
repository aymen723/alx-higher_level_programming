#!/usr/bin/python3
"""listclass."""


class MyList(list):
    """sort for built-in class."""

    def print_sorted(self):
        """print a list sorted ascending."""
        print(sorted(self))
