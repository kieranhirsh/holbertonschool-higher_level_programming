#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []

    for ii in range(len(my_list)):
        if my_list[ii] == search:
            new_list.append(replace)
        else:
            new_list.append(my_list[ii])

    return new_list
