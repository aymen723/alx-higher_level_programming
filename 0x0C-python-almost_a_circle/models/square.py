#!/usr/bin/python3
"""square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """represenation of a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """a constructer for a new square.

        Args:
            size (int): the size of it.
            x (int):the x coordicantion for the new square.
            y (int):the y coordicantion for the new square.
            id (int): id of the new square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getters and setters for the new square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ misa a jour for Square.

        Args:
            *args (ints): attribuate values.
                - 1st arg represent the id
                - 2nd arg represent the size
                - 3rd arg represent the x value
                - 4th arg represent the y value
            **kwargs (dict): New key/value.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dict representation."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,self.width)
