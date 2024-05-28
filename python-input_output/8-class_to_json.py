#!/usr/bin/python3
''' module documentation '''


def class_to_json(obj):
    '''
    This function returns the JSON representation of an object

    Args:
        filename (obj): the object

    Returns:
        JSON representation of the object
    '''
    return (obj.__dict__)
