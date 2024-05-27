#!/usr/bin/python3
''' module documentation '''
import json


def load_from_json_file(filename):
    '''
    This function creates a Python object from a “JSON file”

    Args:
        filename (str): the file read

    Returns:
        filename converted into a Python object
    '''
    with open(filename) as file:
        return json.loads(file.read())
