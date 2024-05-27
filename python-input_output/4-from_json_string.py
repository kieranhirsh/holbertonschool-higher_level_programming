#!/usr/bin/python3
''' module documentation '''
import json


def from_json_string(my_str):
    '''
    This function returns an object represented by a JSON string:

    Args:
        my_str: the JSON string

    Returns:
        my_str converted to a Python data structure
    '''
    return json.loads(my_str)
