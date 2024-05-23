#!/usr/bin/python3
""" a module """


def add_attribute(obj, name, value):
    """
    This function adds a new attribute to an object if possible

    Args:
        obj: the object
        name: the attribute name
        value: the attribute value
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")