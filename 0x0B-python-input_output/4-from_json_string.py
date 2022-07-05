#!/usr/bin/python3
"""Method returns an object represented by
a JSON string
"""
import json


def from_json_string(my_str):
    """Returns my_str represented by JSON string
    Args:
        my_str: string
    """
    return json.loads(my_str)
