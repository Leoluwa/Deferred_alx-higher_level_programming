#!/usr/bin/python3


def print_reversed_list_integer(my_list):
    length_of_list = len(my_list)
    reverse_index = -1

    while reverse_index >= (-length_of_list):
        print("{:d}".format(my_list[reverse_index]))
        reverse_index -= 1
