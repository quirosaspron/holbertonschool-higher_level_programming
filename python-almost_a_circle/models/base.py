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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns a json representation of a list of dictionaries """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ It writes the JSON stirng representation of list_objs to a file """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        dict_list = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as file:
            file.write(cls.to_json_string(dict_list))

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        if cls.__name__ == 'Square':
            dummy = cls(1)
        else:
            dummy = None
        if dummy is not None:
            dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_data = file.read()
                obj_list = cls.from_json_stirng(json_data)
                instances = [cls.create(**obj) for obj in obj_list]
                return instances
        except FileNotFoundError:
            return []
