#!/usr/bin/python3

class Square:
    def __init__(s, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        s.__size = size
    def area(s):
        return (s.__size * s.__size)
