#!/usr/bin/python3
""" module doc for base """
import json


class Base:
    """ class doc for base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ init doc for base """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
