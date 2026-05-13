#!/usr/bin/python3
"""Module that defines a square"""

class Square:
    """Class that defines a square"""
    
    def __init__(self, size=0):
        """Initialize a new Square.
        
        Args:
            size (int): The size of the square.
        """
        self.size = size
        
    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size
        
    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        
    def area(self):
        """Return the current square area."""
        return self.__size ** 2
        
    def my_print(self):
        """Print the square with the character #."""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("#" * self.__size)
