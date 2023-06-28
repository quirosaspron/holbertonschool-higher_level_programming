#!/usr/bin/python3
""" Rectangle class that inherits from Base """
from .base import Base


class Rectangle(Base):
    """ Rectangle class with size, coordinates
        and id attributes """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ The initializer of the class """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ Get width """
        return self.__width

    @property
    def height(self):
        """ Get height """
        return self.__height

    @property
    def x(self):
        """ Get x """
        return self.__x

    @property
    def y(self):
        """ Get y """
        return self.__y

    @width.setter
    def width(self, value):
        """ The setter for width """
        self.__width = value

    @height.setter
    def height(self, value):
        """ The setter for height """
        self.__height = value

    @x.setter
    def x(self, value):
        """ The setter for x """
        self.__x = value

    @y.setter
    def y(self, value):
        """ The setter for y """
        self.__y = value
