#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if str >= 97 and str <= 122:
            i = chr(ord(i) - 32)
        print("{}".format(i), end="")
    print("")
