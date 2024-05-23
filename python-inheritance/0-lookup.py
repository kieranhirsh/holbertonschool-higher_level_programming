#!/usr/bin/python3
""" a module """


def lookup(obj):
    """ Function that returns the list of available attributes
        and methods of an object

    Args:
        obj: an object

    Returns:
        (list): List of attributes
    """
    return dir(obj)
