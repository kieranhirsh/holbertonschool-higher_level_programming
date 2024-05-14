#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0

    for ii in range(x):
        try:
            print(my_list[ii], end="")
        except IndexError:
            break
        else:
            count += 1

    print("")

    return count
