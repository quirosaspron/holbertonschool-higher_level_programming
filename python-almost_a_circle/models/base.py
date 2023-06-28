#!/usr/bin/python3
""" This is the base class, it is a Python
    package and it will be used in all other
    classes of this proyect """
import json


class Base:
    """ The base class, with private attribute __nb_objects,
        the goal of this class is to manage the ID attribute in all
        future cases """

    __nb_objects = 0

    def __init__(self, id=None):
        """ The initializer method, it will initialize id """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ Returns a json representation of a list of dictionaries """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
