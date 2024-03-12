#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        last_number = number % -(10)
        print(-(last_number), end='')
    else:
        last_number = number % 10
        print(last_number, end='')
    return abs(last_number)
