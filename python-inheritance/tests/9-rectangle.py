#!/usr/bin/python3
"""Full rectangle"""


class BaseGeometry:
    """Class Base"""

    def __dir__(self):
        """function __dir__ """
        obj = BaseGeometry
        return dir(obj)

    def area(self):
        """Method area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Method validator"""
        self.name = name
        self.value = value

        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(self.name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(self.name))


class Rectangle(BaseGeometry):
    """class son rectangle"""
    def __init__(self, width, height):
        """Constructor"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """"Methodd area"""
        return (self.__width * self.__height)

    def __str__(self):
        """Method __str__"""
        return ('[Rectangle] {}/{}'.format(self.__width, self.__height))
