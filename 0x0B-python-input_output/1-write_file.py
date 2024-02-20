#!/usr/bin/python3
"""file-writing function."""


def write_file(filename="", text=""):
    """a String to uft8.

    Args:
        filename (str): name of the file.
        text (str): txt to write a file.
    Returns:
        nbr of charcharter.
    """
    with open(filename, "w", encoding="utf-8") as a:
        return a.write(text)
