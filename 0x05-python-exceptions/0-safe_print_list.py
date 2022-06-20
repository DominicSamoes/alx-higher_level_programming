#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_elem = 0
    for e in range(x):
        try:
            print("{}".format(my_list[e]), end="")
            num_elem += 1
        except IndexError:
            break
    print()
    return num_elem
