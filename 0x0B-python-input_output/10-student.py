#!/usr/bin/python3

"""class Student."""

class Student:
    """Represents student."""

    def __init__(self, first_name, last_name, age):
        """Initializes new Student.
        Args:
            first_name (str): The first name
            last_name (str): The last name
            age (int): The age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """representation of the Student.
        If attrs is a list of strings, represents only those attributes
        in the list.
        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(elem) == str for elem in attrs)):
            return {y: getattr(self, y) for y in attrs if hasattr(self, y)}
        return self.__dict__
