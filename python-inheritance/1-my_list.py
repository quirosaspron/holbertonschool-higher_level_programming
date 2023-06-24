#!/usr/bin/python3
""" module inherit list """


class MyList(list):
    """Custom class inheriting from list"""

    def print_sorted(self):
        """Print the list in sorted order"""
        print(sorted(self))
