#!/usr/bin/python3
""" Module Rectangle """


class Rectangle:
    """Rectangle class definded by width and height"""

    def __init__(self, width=0, height=0):
        """Initialize method"""
        if type(width) != int:
            raise TypeError('width must be an integer')
        if type(height) != int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        if width < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = width
            self.__height = height

    @property
    def width(self):
        """Get the width"""
        return(self.__width)

    @width.setter
    def width(self, value):
        """Set the width"""
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """Get the height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Set the height"""
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
