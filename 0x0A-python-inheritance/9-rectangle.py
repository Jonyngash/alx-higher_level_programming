#!/usr/bin/python3
""" Module with Rectangle class """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class Rectangle inherits from BaseGeometry"""

    def __init__(self, width, height):
        """ Constructor """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Compute area """
        return self.__width * self.__height

    def __str__(self):
        """ Return string """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
