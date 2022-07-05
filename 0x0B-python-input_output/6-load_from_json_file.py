#!/usr/bin/python3
"""Method creates an object from a JSON file"""
import json


def load_from_json_file(filename):
    """Creates object from filename"""
    with open(filename) as outfile:
        return json.load(outfile)
