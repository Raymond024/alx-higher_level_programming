#!/usr/bin/python3
"""Defines Rectangle class."""


class Rectangle:
    """Represent rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """set rectangle width."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """set rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return rectangle area."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Returns rectangle printable rep.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        recta = []
        for y in range(self.__height):
            [recta.append('#') for z in range(self.__width)]
            if y != self.__height - 1:
                recta.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Returns rectangle string rep."""
        recta = "Rectangle(" + str(self.__width)
        recta += ", " + str(self.__height) + ")"
        return (recta)

    def __del__(self):
        """Print a message for every rectangle prinnted"""
        print("Bye rectangle...")
