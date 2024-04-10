#!/usr/bin/python3
"""Defines the rectangle"""

class Rectangle:
    """Represents the rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes the rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of rectangle.
        """
        
        self.height = height
        self.width = width

    @property
    def width(self):
        """sets the rectagle width."""
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
        """sets the rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returs the rectangle. area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the rectangle to be printed.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        recta = []
        for y in range(self.__height):
            [recta.append('#') for z in range(self.__width)]
            if y != self.__height - 1:
                recta.append("\n")
        return ("".join(recta))

    def __repr__(self):
        """Return the Rectangle string representation."""
        recta = "Rectangle(" + str(self.__width)
        recta += ", " + str(self.__height) + ")"
        return (recta)
