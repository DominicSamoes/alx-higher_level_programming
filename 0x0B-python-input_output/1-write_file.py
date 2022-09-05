#!/usr/bin/python3
"""Method writes  string to a text file"""


def write_file(filename="", text=""):
    """Method writes tezt to filename

    Args:
        filename: text file name
        text: text to be written to text file
    Returns:
        number of characters written
    """
    with open(filename, "w", encoding="utf-8") as out_file:
        return out_file.write(text)
