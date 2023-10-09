#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This is the documentation for the Square class.
    """

    def __init__(self, size):
        """
        Initialize the Square instance with size.
        """
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Return the string representation of the Square instance.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
