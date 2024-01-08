#!/usr/bin/python3
"""Module for BaseGeometry class."""


class BaseGeometry:
    """The BaseGeometry class."""

    def area(self):
        """Raises an Exception with the following message."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(value))
