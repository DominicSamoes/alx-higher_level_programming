#!/usr/bin/python3
def magic_calculation(a, b):
    res = 0
    for e in range(1, 3):
        try:
            if (e > a):
                raise Exception("Too far")
            else:
                res += (a ** b) / e
        except:
            res = b + a
            break
    return (res)
