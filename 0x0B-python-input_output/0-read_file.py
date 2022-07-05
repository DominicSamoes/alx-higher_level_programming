#!/usr/bin/python3
"""Method reads and prints text file"""


def read_file(filename=""):
    with open(filename, mode='r', encoding="utf-8") as in_file:
        print(in_file.read(), end="")
