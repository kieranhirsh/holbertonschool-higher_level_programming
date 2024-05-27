#!/usr/bin/python3
''' module documentation '''
import json


def to_json_string(my_obj):
    '''
    This function returns the JSON representation of an object

    Args:
        my_obj: the object

    Returns:
        (str): my_obj converted to a JSON string
    '''
    return json.dumps(my_obj)
