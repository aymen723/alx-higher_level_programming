#!/usr/bin/python3
"""a text file reading."""


def read_file(filename=""):
    """Print UTF8."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
