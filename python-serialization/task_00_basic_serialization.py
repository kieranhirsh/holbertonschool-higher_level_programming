#!/usr/bin/python3
''' module documentation '''
import json


def serialize_and_save_to_file(data, filename):
    '''
    function to serialise and save data to a file
    
    Arguments:
        data: the data to serialise
        filename (str): the file to save to
    '''
    with open(filename, "w") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    '''
    This function creates a Python object from a “JSON file”

    Args:
        filename (str): the file read

    Returns:
        filename converted into a Python object
    '''
    with open(filename) as file:
        return json.loads(file.read())
