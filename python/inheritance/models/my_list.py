#!/usr/bin/python3
""" class MyList"""

class MyList(list):
    """ class MyList"""
    def print_sorted(self):
        """sort a list"""
        return self.sort(reverse=False)
