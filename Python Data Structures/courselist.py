"""Name: Dustin Barnes
Course: 2420-001
Project 3 Linked Lists
File: courselist.py

All of the following code was written by me.

This module sets up the courselist class which implements a linked list structure
to hold information about a set of courses."""

from recursioncounter import RecursionCounter

class CourseList():
    """CourseList class is a linked list data structure for a set of courses."""
    def __init__(self):
        """Cunstructor method for the CourseList class, sets up the head of the
        linked list."""
        self.head = None
        self.iter_cursor = None

    def insert(self, course, cursor=None): #pylint: disable=R1710
        """Recursively inserts a course in the correct place in the linked list
        sorted by course number in ascending order."""
        RecursionCounter()
        if cursor is None:
            cursor = self.head
        temp = course
        if self.head is None or temp.course_number <= self.head.course_number:
            temp.next = self.head
            self.head = temp
            return
        if cursor.next is not None and temp.course_number <= cursor.next.course_number and temp.course_number > cursor.course_number: #pylint: disable=C0301
            temp.next = cursor.next
            cursor.next = temp
            return
        if cursor.next is None:
            temp.next = None
            cursor.next = temp
            return
        cursor = cursor.next
        return self.insert(course, cursor)

    def remove(self, course_number, cursor=None): #pylint: disable=R1710
        """Recursively removes the first occurance of the given course number
        from the linked list."""
        RecursionCounter()
        if cursor is None:
            cursor = self.head
        if self.head is None:
            return "list is empty"
        if cursor == self.head and cursor.course_number == course_number:
            self.head = cursor.next
            return
        if cursor.next is not None and cursor.next.course_number == course_number:
            cursor.next = cursor.next.next
            return
        if cursor.next is None and cursor.course_number != course_number:
            return
        return self.remove(course_number, cursor.next)

    def remove_all(self, course_number, cursor=None): #pylint: disable=R1710
        """Recursively removes all occurances of the given course number
        from the linked list."""
        RecursionCounter()
        if cursor is None:
            cursor = self.head
        if self.head is None:
            return "list is empty"
        if cursor == self.head and cursor.course_number == course_number:
            self.head = cursor.next
            cursor = self.head
            return self.remove_all(course_number, cursor)
        if cursor.next is not None and cursor.next.course_number == course_number:
            cursor.next = cursor.next.next
            return self.remove_all(course_number, cursor)
        if cursor.next is None:
            return
        if cursor.next.next is None and cursor.next.course_number == course_number:
            cursor.next = cursor.next.next
        return self.remove_all(course_number, cursor.next)

    def find(self, course_number, cursor=None):
        """Finds and returns the given course number in the linked list,
        if there is no course of that number it will return a -1"""
        RecursionCounter()
        if cursor is None:
            cursor = self.head
        if self.head is None:
            return "list is empty"
        if cursor == self.head and cursor.course_number == course_number:
            return cursor
        if cursor.next is not None and cursor.next.course_number == course_number:
            return cursor.next
        if cursor.next is None:
            return -1
        return self.find(course_number, cursor.next)

    def size(self, cursor=None, list_size=0):
        """Recursively counts and returns the number of elements in the linked list."""
        RecursionCounter()
        if cursor is None:
            cursor = self.head
        if self.head is None:
            return 0
        if cursor.next is None:
            list_size += 1
            return list_size
        list_size += 1
        return self.size(cursor.next, list_size)

    def calculate_gpa(self, gpa_sum=0.0, credit_hr_sum=0.0, cursor=None):
        """Recursively counts and calculates the weighted gpa for the set of courses
        in the linked list."""
        RecursionCounter()
        if cursor is None:
            cursor = self.head
        if self.head is None:
            return 0.0
        gpa_sum += cursor.grade() * cursor.credit_hr()
        credit_hr_sum += cursor.credit_hr()
        if cursor.next is None:
            overall_gpa = gpa_sum/credit_hr_sum
            return overall_gpa
        return self.calculate_gpa(gpa_sum, credit_hr_sum, cursor.next)

    def is_sorted(self, cursor=None):
        """Recursively Tests to see if the linked list is sorted. If it is, returs True,
        if it is not returns False."""
        RecursionCounter()
        if cursor is None:
            cursor = self.head
        if self.head is None:
            return True
        if cursor.next is None:
            return True
        if cursor.course_number > cursor.next.course_number:
            return False
        return self.is_sorted(cursor.next)

    def __str__(self):
        """Creates the string representation of the linked list
        giving each courses information."""
        output = ""
        cursor = self.head
        while cursor is not None:
            output += f'{cursor}\n'
            cursor = cursor.next
        return output

    def __iter__(self):
        """Sets up the linke lists iteration."""
        self.iter_cursor = self.head
        return self

    def __next__(self):
        """Sets up the next function when dealing with iteration
        in the linked list."""
        if self.iter_cursor is None:
            raise StopIteration
        course = self.iter_cursor
        self.iter_cursor = self.iter_cursor.next
        return course
