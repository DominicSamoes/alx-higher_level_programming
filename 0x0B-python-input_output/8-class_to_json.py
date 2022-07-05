#!/usr/bin/python3
"""Method returns the dictionary description
for JSON serialization of an object
"""


def class_to_json(obj):
    """Return dictionary representation of a 
    simple data structure
    """
    return obj.__dict__
