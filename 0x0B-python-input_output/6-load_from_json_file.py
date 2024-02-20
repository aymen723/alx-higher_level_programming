#!/usr/bin/python3
"""function to file read json."""
import json


def load_from_json_file(filename):
    """from json to python object."""
    with open(filename) as f:
        return json.load(f)
