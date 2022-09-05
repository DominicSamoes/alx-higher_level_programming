#!/usr/bin/python3
"""Method writes an object to a text file,
using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes my_obj to filename using a
    JSON representation
    Args:
        my_obj: object
        filename: text file
    """
    with open(filename, "w") as outfile:
        json.dump(my_obj, outfile)
