#!/usr/bin/python3
""" a class Square that inherits from the Rectangle class """
from .rectangle import Rectangle


class Square(Rectangle):
    """ Square is a class that inherits the Rectangle class """
    def __init__(self, size, x=0, y=0, id=None):
        """ The class initializer """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Prints something method """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """ The size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ The size setter """
        if type(value) is not int:
            raise TypeError('width must be integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        else:
            self._Rectangle__width = value
            self._Rectangle__height = value

    def update(self, *args, **kwargs):
        """ Class to allow attributes to be updated """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.size = args[1]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) >= 4:
            self.y = args[3]
        elif len(kwargs) > 0:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
