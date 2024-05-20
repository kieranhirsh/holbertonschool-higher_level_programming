#!/usr/bin/python3
''' say_my_name module '''


def say_my_name(first_name, last_name=""):
    ''' this function prints a name

    Args:
        first_name (str): a first name
        last_name (str, optional): a last name
    '''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
