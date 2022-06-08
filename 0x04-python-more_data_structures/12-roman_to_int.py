#!/usr/bin/python3
def sub(list_num):
    subt = 0
    maxlist = max(list_num)

    for i in list_num:
        if maxlist > i:
            subt += i

    return (maxlist - subt)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    romnum = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    keys_list = list(romnum.keys())

    count = 0
    lastrom = 0
    listnum = [0]

    for c in roman_string:
        for r in keys_list:
            if r == c:
                if romnum.get(c) <= lastrom:
                    count += sub(listnum)
                    listnum = [romnum.get(c)]
                else:
                    listnum.append(romnum.get(c))

                lastrom = romnum.get(c)

    count += sub(listnum)

    return (count)
