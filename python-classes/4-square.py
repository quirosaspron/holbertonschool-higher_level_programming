#!/usr/bin/python3
"""Module Square"""


class Square:
    """Square class defined by geometric shape. Attributes: size(int)"""

    def __init__(self, size=0):
        """Initialize method"""
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
    def area(self):
        """Area method: Returns the square's area"""
        return (self.__size**2)
    @property
    def size(self):
        """Getting the size method. Returns the size of the square"""
        return (self.__size)
    @size.setter
    def size(self, value):
        """Setting the size method. Lets you set the size of the square"""
        if type(value) != int:
            raise TypeError('size must be an integer'
        if value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value
