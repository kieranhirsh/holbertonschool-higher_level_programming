#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sort_dic = sorted(a_dictionary)

    for ii in range(len(sort_dic)):
        print("{0}: {1}".format(sort_dic[ii], a_dictionary.get(sort_dic[ii])))
