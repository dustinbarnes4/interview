"""Name: Dustin Barnes
Course: 2420-001
Project 4 Stacks
File: stack.py
The following code was written by me. """

class Stack():
    """Stack class, uses a list to perform the tasks of a stack."""
    def __init__(self):
        """Constructs the object with an empty list forming the stack."""
        self.data = []

    def push(self, item):
        """Puts an item on top of the stack."""
        self.data.append(item)

    def pop(self):
        """Removes and returns the top item of the stack."""
        if len(self.data) == 0:
            raise IndexError("the stack is empty")
        return self.data.pop()

    def peek(self):
        """Returns the top item of the stack but does not remove it."""
        if len(self.data) == 0:
            raise IndexError("the stack is empty")
        return self.data[-1]

    def size(self):
        """Returns the size of the stack."""
        return len(self.data)

    def is_empty(self):
        """Returns a bool value to determine if the stack has items in it or not."""
        if self.size() == 0:
            return True
        return False

    def clear(self):
        """Resets the stack to an empty stack."""
        self.data = []
        