#!/usr/bin/python3
"""Finds peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds peak in list_of_integers"""

    if list_of_integers is None or list_of_integers == []:
        return None
    l = 0
    h = len(list_of_integers)
    m = ((h - l) // 2) + l
    m = int(m)
    if h == 1:
        return list_of_integers[0]
    if h == 2:
        return max(list_of_integers)
    if list_of_integers[mid] >= list_of_integers[m - 1] and\
            list_of_integers[m] >= list_of_integers[m + 1]:
        return list_of_integers[m]
    if m > 0 and list_of_integers[m] < list_of_integers[m + 1]:
        return find_peak(list_of_integers[m:])
    if m > 0 and list_of_integers[m] < list_of_integers[m - 1]:
        return find_peak(list_of_integers[:m])
