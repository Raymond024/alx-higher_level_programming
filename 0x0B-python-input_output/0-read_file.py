#!/usr/bin/python3

"""Discribres text file-reading function"""

def read_file(filename=""):
    """Prints the contents of text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
