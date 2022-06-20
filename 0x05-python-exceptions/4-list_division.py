#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    quot_list = []
    for q in range(list_length):
        try:
            quot = my_list_1[q] / my_list_2[q]
        except TypeError:
            print("wrong type")
            quot = 0
        except ZeroDivisionError:
            print("division by 0")
            quot = 0
        except IndexError:
            print("out of range")
            quot = 0
        finally:
            quot_list.append(quot)
    return (quot_list)
