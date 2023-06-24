#!/usr/bin/python3
""" Base geometry module """


class BaseGeometry:
    """ Class with empty implementation of area """

    def area(self):
        """ An empty implementation of area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates a value """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
