#!/usr/bin/python3
"""Module Square"""


class Square:
    """Square class defined by geometric shape. Attributes: size(int)"""

    def __init__(self, size):
        """Initialize method. Args: size(int)"""
        self.__size = size
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0'
