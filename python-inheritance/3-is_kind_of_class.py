#!/usr/bin/python3
""" instance of a class """


def is_kind_of_class(obj, a_class):
    """ Returns True if the obj is an instance of a class
     (or a class that inherited from) or otherwise False """

    return isinstance(obj, a_class)
