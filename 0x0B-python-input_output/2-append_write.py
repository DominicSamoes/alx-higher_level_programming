#!/usr/bin/python3
"""Method appends string to end of file"""


def append_write(filename="", text=""):
    """Appends text to filename
    Args:
        filename: name of text file
        text: text to be appended
    Returns:
        the number of characters
    """
    with open(filename, "a", encoding="utf-8") as outfile:
        return outfile.write(text)
