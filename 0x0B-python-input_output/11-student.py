#!/usr/bin/python3
"""a Student class."""


class Student:
    """a student."""

    def __init__(self, first_name, last_name, age):
        """contructer for a Student.

        Args:
            first_name (str): first name for student.
            last_name (str): last name for student.
            age (int): age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """A Dict repert a of the Student.

        represents only those attributes.
        Args:
            attrs (list): att to reprt.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace attrib of student.

        Args:
            json (dict): to repalce with attribute.
        """
        for k, v in json.items():
            setattr(self, k, v)
