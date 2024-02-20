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

    def to_json(self):
        """dict reprt of a student."""
        return self.__dict__
