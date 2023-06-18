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

    def area(self):
        """Get the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Get the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (self.__width*2 + self.__height*2)

    def __str__(self):
        """Print the rectangle"""
        if self.area() == 0:
            return('')
        else:
            return (('#'*self.__width + "\n")*self.__height)[:-1]
        
