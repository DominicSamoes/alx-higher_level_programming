#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    listorder = list(a_dictionary)
    listorder.sort()
    for i in listorder:
        print("{}: {}".format(i, a_dictionary.get(i)))
