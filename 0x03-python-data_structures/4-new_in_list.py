#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        list = my_list
        return (list)
    elif idx > (len(my_list) - 1):
        list = my_list
        return (list)
    my_list.insert(idx, element)
    return (my_list)
