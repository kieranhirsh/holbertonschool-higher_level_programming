#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    div_list = [None] * list_length
    for ii in range(list_length):
        try:
            div_list[ii] = my_list_1[ii] / my_list_2[ii]
        except IndexError:
            print("out of range")
            div_list[ii] = 0
        except TypeError:
            print("wrong type")
            div_list[ii] = 0
        except ZeroDivisionError:
            print("division by 0")
            div_list[ii] = 0

    return div_list