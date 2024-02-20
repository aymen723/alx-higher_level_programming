#!/usr/bin/python3
"""function for file-appending."""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file.

    Args:
        filename (str): name of the file.
        text (str): str to append.
    Returns:
        nbr of charchter to append.
    """
    with open(filename, "a", encoding="utf-8") as a:
        return a.write(text)
