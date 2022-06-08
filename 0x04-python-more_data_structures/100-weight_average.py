#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    count = 0
    de = 0
    for t in my_list:
        count += t[0] * t[1]
        de += t[1]
    return (count / de)
