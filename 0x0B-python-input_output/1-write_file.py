#!/usr/bin/python3

"""Discribes file-writing function."""

def write_file(filename="", text=""):
    """Write string to text file.
    Args:
        filename (str): The name of the file
        text (str): The text to write 
    Returns:
        number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
