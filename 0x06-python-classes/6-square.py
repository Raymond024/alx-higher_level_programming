#!/usr/bin/python3


class Square:

    def __init__(s, size=0, position=(0,0)):
        s.size = size
        s.position = position

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

    @property
    def position(s):

        return (s.__position)

    @position.setter
    def position(s, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        s.__position = value

    def area(s):
        
        return (s.__size * s.__size)

    def my_print(s):
        
        if s.__size == 0:
            print("")
            return

        [print("") for i in range(0, s.__position[1])]
        for i in range(0, s.__size):
            [print(" ", end="") for j in range(0, s.__position[0])]
            [print("#", end="") for k in range(0, s.__size)]
            print("")
