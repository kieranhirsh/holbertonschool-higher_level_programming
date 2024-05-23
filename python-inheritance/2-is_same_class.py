#!/usr/bin/python3
""" a module """


def is_same_class(obj, a_class):
    '''
    function that checks if obj is exactly an instance of the specified class

    Returns:
        True, if same
        False, otherwise
    '''
    return type(obj) is a_class
