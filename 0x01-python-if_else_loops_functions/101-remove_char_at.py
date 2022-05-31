#!/usr/bin/python3
def remove_char_at(str, n):
    ch = ""
    for counter in range(len(str)):
        if counter != n:
            ch += str[counter]
    return (ch)
