#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dictionary = {}

    for key in a_dictionary:
        new_dictionary[key] = 2 * a_dictionary[key]

    return new_dictionary
