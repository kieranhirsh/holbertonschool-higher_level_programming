#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sort_dict = sorted(a_dictionary)

    for ii in range(len(sort_dict)):
        print("{0}: {1}".format(sort_dict[ii], a_dictionary.get(sort_dict[ii])))
