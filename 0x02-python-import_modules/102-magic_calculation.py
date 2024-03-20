#!/usr/bin/python3

def magic_calculation(a, b):
    """Match bytecode provided by Holberton School."""
    from magic_calculation_102 import add, sub

    if a < b:
        y = add(a, b)
        for x in range(4, 6):
            y = add(y, x)
        return (y)

    else:
        return(sub(a, b))
