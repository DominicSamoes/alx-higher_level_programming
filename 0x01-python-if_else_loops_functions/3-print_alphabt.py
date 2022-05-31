#!/usr/bin/python3
"""Prints the ASCII alphabet in lowercase"""
for lc in range(97, 123):
    if lc != 101 and lc != 113:
        print("{:c}".format(lc), end="")
