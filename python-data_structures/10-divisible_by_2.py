#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    truth = []
    for ii in range(len(my_list)):
        truth.append(my_list[ii] % 2 == 0)

    return truth
