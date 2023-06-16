#!/usr/bin/python3
"""Module Square"""


class Square:
    """Square class defined by geometric shape. Attributes: size(int)"""

    def __init__(self, size=0):
        """Initialize method"""
        self.__size = size
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
    def area(self):
        """Area method: Returns the square's area"""
        return (size**2)
