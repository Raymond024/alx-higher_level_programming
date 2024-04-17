#!/usr/bin/python3
"""function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """Adds a new attribute to an object if possible.
    Args:
        obj (any): The object to add to
        att (str): The name of the attribute to add
        value (any): The value to add
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
