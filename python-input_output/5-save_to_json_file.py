#!/usr/bin/python3
''' module documentation '''
import json


def save_to_json_file(my_obj, filename):
    '''
    This function writes an object to a text file, using a JSON representation:

    Args:
        my_obj: the object
        filename: the text file
    '''
    with open(filename, "w") as file:
        return file.write(json.dumps(my_obj))
