#!/usr/bin/python3
""" inherits from """


def inherits_from(obj, a_class):
    """ Returns True if the obj is an instance of a class
     that inherited from; otherwise False """

    return issubclass(obj, a_class)
