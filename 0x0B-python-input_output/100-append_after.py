#!/usr/bin/python3

"""text file insertion function."""

def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line in a file.
    Args:
        filename (str): The file name
        search_string (str): The string to search for
        new_string (str): string to insert.
    """
    text = ""
    with open(filename) as y:
        for line in y:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as x:
        x.write(text)
