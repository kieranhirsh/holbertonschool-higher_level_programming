#!/usr/bin/python3

def max_integer(my_list=[]):
    max = 0
    for ii in range(0,len(my_list)):
        if my_list[ii] > max:
            max = my_list[ii]

    return max
