#!/usr/bin/python3
"""Module Square"""


class Square:
    """Square class defined by geometric shape. Attributes: size(int)"""

    def __init__(self, size=0, position=(0,0)):
        """Initialize method"""
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
        if type(position) != tuple or len(position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(position[0]) != int or position[0] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(position[1]) != int or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
           self.__position = position

    def area(self):
        """Area method: Returns the square's area"""
        return (self.__size**2)

    @property
    def size(self):
        """Getting the size method. Returns the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setting the size method. Lets you set the size of the square"""
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        """Getting the position method. Returns the position of the square"""
        return(self.__position)

    @position.setter
    def position(self, value):
        """Setting the position method. Lets you set the position of the square"""
        if type(value) != tuple or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(value[0]) != int or value[0] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(value[1]) != int or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
           self.__position == position

    def my_print(self):
        """Method to print the square with # symbols"""
        if self.__size == 0:
            print('')
        else:
            for n in range(self.__position[1]):
                print()
            for r in range(self.__size):
                for n in range(self.__position[0]):
                    print(' ', end ='')
                for c in range(self.__size):
                    print('#', end = '')
                print()
