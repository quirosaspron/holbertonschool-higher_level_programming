#!/usr/bin/python3
"""  Rectangle module """
BaseGeometry = __import__('7-base_geometry').BaseGeometry



class Rectangle(BaseGeometry):
    """ Class htat inherits form BaseGeometry """

    __init__(self, width, height):
        """ Initializator """

        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height