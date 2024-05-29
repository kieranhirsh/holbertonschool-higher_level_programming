#!/usr/bin/python3
''' module documentation '''
import csv
import json


def convert_csv_to_json(filename):
    '''
    function to take data from a csv file and saves it to a json file
    
    Arguments:
        filename (str): the file to read from

    Returns:
        True, if conversion was successful
        False, otherwise
    '''
    data = []
    try:
        with open(filename) as csv_file:
            for row in csv.DictReader(csv_file):
                data.append(row)

        with open("data.json", "w") as json_file:
            json.dump(data, json_file)

        return True
    except Exception:
        return False
