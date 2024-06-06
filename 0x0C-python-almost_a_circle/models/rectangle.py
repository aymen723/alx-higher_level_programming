#!/usr/bin/python3
"""a class for rectangle."""
from models.base import Base


class Rectangle(Base):
    """a class represenation for a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """the constructor for rectengle object.

        Args:
            width (int): width for rectengale obj.
            height (int): height for rectengale obj.
            x (int): x cooradiante value for rectengale obj.
            y (int): y cooradiante value for rectengale obj.
            id (int): id for the object.
        Raises:
            TypeError: if width and height are not an int.
            ValueError: if width or height <= 0.
            TypeError: Iif x and y are not an int.
            ValueError: and if x and y are <=0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getters and setters for width the new rectngale object."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getters and setters for height the new rectngale object."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getters and setters for x vale the new rectngale object."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getters and setters for y value the new rectngale object."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """a function that give the area."""
        return self.width * self.height

    def display(self):
        """a function that print the Rectangle with #."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """misa a jour for the Rectangle.

        Args:
            *args (ints): attribuate values.
                - 1st arg represent the id
                - 2nd arg represent the width
                - 3rd arg represent the height
                - 4th arg represent the x value
                - 5th arg represent the y value
            **kwargs (dict): New key/value.
        """
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1

        elif kwargs and len(kwargs) != 0:
            for j, b in kwargs.items():
                if j == "id":
                    if b is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = b
                elif j == "width":
                    self.width = b
                elif j == "height":
                    self.height = b
                elif j == "x":
                    self.x = b
                elif j == "y":
                    self.y = b

    def to_dictionary(self):
        """a function that give the dictionary representation."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """a function that give the print() and str() of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,self.x, self.y,self.width, self.height)
