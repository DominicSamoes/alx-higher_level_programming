#!/usr/bin/python3
"""Method inserts a line of text to a file,
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """Insert new_string after each line search_string
    Args:
        filename: name of text file
        search_string: string to search for within the file
        new_string: string to be inserted
    """
    with open(filename, "r") as readfile:
        text = readfile.readlines()

    with open(filename, "w") as outfile:
        strng = ""
        for line in text:
            strng += line
            if search_string in line:
                strng += new_string
            outfile.write(strng)
