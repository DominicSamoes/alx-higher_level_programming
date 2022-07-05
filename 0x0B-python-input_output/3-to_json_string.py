#!/usr/bin/python3
"""Method returns JSON representation of an object"""
import json


def to_json_string(my_obj):
    """Method returns JSON representation of my_obj
    Args:
        my_obj: object/string
    Returns:
        JSON representation
    """
    return json.dumps(my_obj)
