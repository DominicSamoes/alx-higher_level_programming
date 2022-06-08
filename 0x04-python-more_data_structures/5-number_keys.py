#!/usr/bin/python3
def number_keys(a_dictionary):
    count = 0
    keys_list = list(a_dictionary.keys())
    for i in keys_list:
        count += 1
    return (count)
