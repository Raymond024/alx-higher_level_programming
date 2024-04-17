#!/usr/bin/python3

"""file-appending function."""

def append_write(filename="", text=""):
    """Appends string to end of a UTF8 text file.
    Args:
        filename (str): The name of the file
        text (str): The string to append
    Returns:
        number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
