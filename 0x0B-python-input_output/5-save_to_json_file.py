#!/usr/bin/python3
"""Defines a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """object to json repr."""
    with open(filename, "w") as a:
        json.dump(my_obj, a)
