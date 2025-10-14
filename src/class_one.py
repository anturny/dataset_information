#! /usr/bin/python3

##--------------------------------------------------------------------\
#   minimum_python_example
#   './minimum_python_example/src/class_one.py'
#
#   This is an example of a simple class that takes no inputs for initialization.
#       An array is created at init() and can be manipulated by outside calls.
#
#   Author(s): Lauren Linkous
#   Last update: January 19, 2024
##--------------------------------------------------------------------\

class ClassOne:
    # The constructor (__init__) initializes an empty list called myArray
    def __init__(self):
        self.myArray = []  # This list will hold numbers added to it

    # The clearAray function clears all elements in myArray
    def clearAray(self):
        self.myArray = []  # Reset the list to an empty list

    # The addNumber function appends a number to the myArray list
    def addNumber(self, n):
        self.myArray.append(n)  # Add the number n to the end of the list

    # The getArray function returns the current state of the myArray list
    def getArray(self):
        return self.myArray  # Return the list of numbers currently stored
