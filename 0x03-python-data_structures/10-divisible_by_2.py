#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    next_list = []
    if my_list:
        for digit in my_list:
            next_list.append(False if digit % 2 else True)
        return next_list
