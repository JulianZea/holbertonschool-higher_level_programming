#!/usr/bin/python3
"""
First Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    class inherits Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        Base.__init__(self, id)

    @property
    def width(self):
        """
        private instance width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        private instance
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """
        private instance
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        private instance
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """
        private instance
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        private instance
        """
        if type(value) is not int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """
        private instance
        """
        return self.__y

    @y.setter
    def y(self, value):
        """private instance"""
        if type(value) is not int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """
        returns the area value of the Rectangle instance
        """
        return self.height * self. width
