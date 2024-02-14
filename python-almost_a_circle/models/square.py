#!/usr/bin/python3
""" Square class """
from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class inherits from Rectangle class"""
    # constructor

    def __init__(self, size, x=0, y=0, id=None):
        """ init method for square class
        Args:
            size (int): size of the square
            x (int): x position of the square
            y (int): y position of the square
            id (int): id of the square
        """
        super().__init__(size, size, x, y, id)
        
    def __str__(self):
        """ string representation of square """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Getter for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size, updates both width and height."""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns the string representation of the Square instance."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
