#!/usr/bin/python3
"""Square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class, inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of Square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.check_int("width", value)
        self.check_positive("width", value)
        self.width = value

    def update(self, *args, **kwargs):
        """Update attributes of the Square"""
        if len(args) == 0:
            id = kwargs.get("id", self.id)
            self.id = id
            size = kwargs.get("size", self.width)
            x = kwargs.get("x", self.x)
            y = kwargs.get("y", self.y)
        else:
            self.id = args[0] if len(args) >= 1 else self.id
            size = args[1] if len(args) >= 2 else self.width
            x = args[2] if len(args) >= 3 else self.x
            y = args[3] if len(args) >= 4 else self.y
        self.checks(size, size, x, y)
        self.width = size
        self.x = x
        self.y = y

    def to_dictionary(self):
        """Return dictionary representation of Square"""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
