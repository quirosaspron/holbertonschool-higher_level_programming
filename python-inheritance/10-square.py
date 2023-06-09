#!/usr/bin/python3
"""Square module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Just a simple square, nothing to see here """
    def __init__(self, size):
        """ Just an initializer """
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        """ Implementatiion of area method """
        return (self.__size**2)

    def __str__(self):
        """ Printing method """
        return (f"[Rectangle] {self.__size}/{self.__size}")
