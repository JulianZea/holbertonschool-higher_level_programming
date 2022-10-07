#!/usr/bin/python3
"""
The square
"""
from models.rectangle import Rectangle
from models.base import Base


class Square(Rectangle):
    """
    class Square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        constructor
        """
        super().__init__(size, size, x, y, id)
        self.__width = size

    def __str__(self):
        """
        str
        """
        return('[Square] ({}) {}/{} - {}'
               .format(self.id, self.x, self.y, self.__width))

    @property
    def size(self):
        """
        private instance size
        """
        return self.__width

    @size.setter
    def size(self, value):
        """
        private instance
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value
            self.__height = value
