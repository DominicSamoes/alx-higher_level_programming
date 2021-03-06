#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """Prints name and surname

    Args:
        first_name: first name
        last_name: surname/last name

    Returns:
        No return

    Raises:
        TypeError: If either arg is not a string

    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
