#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_new = my_list[:]
    if 0 <= idx < len(my_list):
        list_new[idx] = element
    return (list_new)
