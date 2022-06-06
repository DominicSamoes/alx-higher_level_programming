#!/usr/bin/env/python3
def no_c(my_string):
    leng = len(my_string)
    a = 0
    strng = my_string[:]
    for b in range(leng):
        if (my_string[b] == 'c' or my_string[b] == 'C'):
            strng = strng[:(b - a)] + my_string[(b + 1):]
            a += 1
    return (strng)
