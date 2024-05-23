#!/usr/bin/python3
""" a module """


def is_kind_of_class(obj, a_class):
    '''
    function that checks is obj is is an instance of, or is an instance of a
    class that inherited from, the specified class

    Returns:
        True, is same
        False, otherwise
    '''
    return isinstance(obj, a_class)
