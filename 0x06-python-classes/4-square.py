#!/usr/bin/python3

class Square:
    def __init__(s, size=0):
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
