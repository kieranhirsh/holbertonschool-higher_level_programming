#!/usr/bin/python3
""" a module """


def is_kind_of_class(obj, a_class):
    '''
    function that checks if obj is an instance of a class that inherited
    (directly or indirectly) from the specified class 

    Returns:
        True, if true
        False, otherwise
    '''
    return issubclass(obj, a_class) and not type(obj) is a_class
