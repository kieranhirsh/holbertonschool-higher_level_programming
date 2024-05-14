#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    delete = []

    for ii in a_dictionary:
        if a_dictionary[ii] == value:
            delete.append(ii)

    for ii in delete:
        del a_dictionary[ii]

    return a_dictionary
