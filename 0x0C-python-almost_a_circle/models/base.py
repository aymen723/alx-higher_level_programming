#!/usr/bin/python3

"""Defines a base model class."""
import json
import csv
import turtle


class Base:
    """base class model.

    This is the represenation base class model for the rest of the models in this project*.

    Private Class Attributes:
        __nb_object (int): represent the number if instation.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """constructer for the base class.

        Args:
            id (int): the id of base class instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """a function that take json serialisaziton of a list.

        Args:
            list_dictionaries (list): list of dict.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """a function that a json list to a file.

        Args:
            list_objs (list): list of base object.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """a function that give a deserialisaztion of json.

        Args:
            json_string (str): a sjon string.
        Returns:
            incase json_string doesnt exist - an empty list.
            Otherwise - a list.            
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a object from a dict.

        Args:
            **dictionary (dict): pair values of attributes.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Return a list of object from json.

        Reads from `filewithjsonextention.json`.

        Returns:
            incase file doesnt exist - an empty list.
            Otherwise - a list of objects.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []