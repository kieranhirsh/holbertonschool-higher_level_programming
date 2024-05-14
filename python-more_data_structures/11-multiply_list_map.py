#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    def mult(n):
        return n * number

    return list(map(mult, my_list))
