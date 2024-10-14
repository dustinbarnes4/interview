"""Name: Dustin Barnes
Course: 2420-001
Project 3 Linked Lists
File: course.py

All of the following code was written by me.

This module sets up the course class for use within the course list module."""

class Course():
    """Course class, sets up a course object to hold the course information including
    the name, number credit hours, and grade."""
    def __init__(self, course_number=0, course_name="", course_credit_hr=0.0, course_grade=0.0):
        """Initializes the course object with default values for all variables.
        Checks to make sure non default variables are the correct type."""
        if not isinstance(course_number, int):
            raise ValueError("course number must be an integer")
        if course_number < 0:
            raise ValueError("course number must not be negative")
        if not isinstance(course_name, str):
            raise ValueError("course name must be a string")
        if not isinstance(course_credit_hr, float):
            raise ValueError("course credit hours must be a float")
        if course_credit_hr < 0:
            raise ValueError("course credit hours must not be negative")
        if not isinstance(course_grade, float):
            raise ValueError("course grade must be a float")
        if course_grade < 0:
            raise ValueError("course grade must not be negative")
        self.course_number = int(course_number)
        self.course_name = course_name
        self.course_credit_hr = float(course_credit_hr)
        self.course_grade = float(course_grade)
        self.next = None

    def number(self):
        """Returns the course number on call."""
        return self.course_number

    def name(self):
        """Returns the course name on call."""
        return self.course_name

    def credit_hr(self):
        """Returns the course credit hours on call."""
        return self.course_credit_hr

    def grade(self):
        """Returns the course grade on call."""
        return self.course_grade

    def __str__(self):
        """Sets the string representation of the class to give course information."""
        return "cs" + str(self.course_number) + " " + str(self.course_name) + " Grade: " + str(self.course_grade) + " Credit Hours: " + str(self.course_credit_hr) #pylint: disable=C0301
