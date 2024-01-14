#!/usr/bin/python3
"""Base module"""
import json


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Base class constructor"""
        if id is not None:
            self.id = id
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts list of dictionaries to JSON string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save list of objects to a file in JSON format"""
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding="utf-8") as f:
            list_data = []
            if list_objs is None or len(list_objs) == 0:
                json.dump(json.loads(cls.to_json_string(list_data)), f)
            else:
                for obj in list_objs:
                    list_data.append(obj.to_dictionary())
                json.dump(json.loads(cls.to_json_string(list_data)), f)

    @staticmethod
    def from_json_string(json_string):
        """Converts JSON string to list of dictionaries"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance with attributes set from a dictionary"""
        if cls.__name__ == "Square":
            dummy = cls(1)
        elif cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Loads objects from a file in JSON format"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, encoding="utf-8") as f:
                new_list = []
                dict_list = cls.from_json_string(json.dumps(json.load(f)))
                for element in dict_list:
                    new_list.append(cls.create(**element))
                return new_list
        except FileNotFoundError:
            return []
