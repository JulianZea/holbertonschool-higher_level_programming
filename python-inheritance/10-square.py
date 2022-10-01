#!/usr/bin/python3
"""Square #1"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class son rectangle"""
    def __init__(self, width, height):
        """Constructor"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """"Methodd area"""
        return self.__width * self.__height

    def __str__(self):
        """Method __str__"""
        return ('[Rectangle] {}/{}'.format(self.__width, self.__height))


class Square(Rectangle):
    """class square"""
    def __init__(self, size):
        """Constructor"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(self.__size, self.__size)
