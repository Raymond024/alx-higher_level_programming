#!/usr/bin/python3

class Square:
    def __init__(s, size):
        s.size = size
    @property
    def size(s):
        return (s.__size)

    @size.setter
    def size(s, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        s.__size = value

    def area(s):
        return (s.__size * s.__size)

    def my_print(s):
        for x in range(0, s.__size):
            [print("#", end="") for y in range(s.__size)]
            print("")
        if s.__size == 0:
            print("")
