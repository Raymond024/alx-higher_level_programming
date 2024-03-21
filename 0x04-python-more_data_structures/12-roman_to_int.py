#!/usr/bin/python3
def roman_to_int(roman_string: str):
    if roman_string is None or type(roman_string) != str:
        return 0
    data = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    nums = [data[z] for z in roman_string] + [0]
    r = 0

    for x in range(len(nums) - 1):
        if nums[x] >= nums[x+1]:
            r += nums[x]
        else:
            r -= nums[x]

    return r
