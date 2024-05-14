#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    weighted_sum = 0
    weights = 0
    for ii in range(len(my_list)):
        weighted_sum += my_list[ii][0] * my_list[ii][1]
        weights += my_list[ii][1]

    return weighted_sum / weights
