#!/usr/bin/python3
"""Method reads and prints from text file"""


def read_file(filename=""):
    """Method reads from filename
    and prints to stdout
    Args:
        filename: name of text file
    """
    with open(filename, mode='r', encoding="utf-8") as in_file:
        print(in_file.read(), end="")
