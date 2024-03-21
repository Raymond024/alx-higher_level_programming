#!/usr/bin/python3
def complex_delete(my_dict, value):
    temp = my_dict.copy()
    for x, y in temp.items():
        if value == y:
            my_dict.pop(x)
    return my_dict
