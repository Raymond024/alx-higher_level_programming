#!/usr/bin/python3
'''Module for MyList'''

class MyList(list):
    '''Custom MyList '''
    def print_sorted(self):
        '''For printing sorted list.'''
        print(sorted(self))
