#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if str <= 122 and str >= 97:
            i = chr(ord(i) - 32)
        print("{}".format(i), end="")
    print("")
