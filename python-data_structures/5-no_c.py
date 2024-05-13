#!/usr/bin/python3

def no_c(my_string):
    for ii in range(len(my_string)):
        if my_string[ii] == 'c' or my_string[ii] == 'C':
            if ii == len(my_string):
                my_string = my_string[0:ii]
                return my_string
            else:
                my_string = my_string[0:ii] + no_c(my_string[ii + 1:])
                return my_string

    return my_string
