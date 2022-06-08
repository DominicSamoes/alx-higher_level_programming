#!/usr/bin/python3
def uniq_add(my_list=[]):
    list_my = set(my_list)
    summation = 0
    for i in list_my:
        summation += i
    return (summation)
