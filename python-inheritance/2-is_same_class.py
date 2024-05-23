#!/usr/bin/python3
""" a module """


def is_same_class(obj, a_class):
    '''
    function that checks is obj is exactly an instance of the specified class

    Returns:
        True, is same
        False, otherwise
    '''
    return type(obj) == a_class
