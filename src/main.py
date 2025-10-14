#! /usr/bin/python3

##--------------------------------------------------------------------\
#   minimum_python_example
#   './minimum_python_example/src/main.py'
#
#   This is an example of an entry point for this Python project. 
#
#   Author(s): Lauren Linkous
#   Last update: January 19, 2024
##--------------------------------------------------------------------\

# imports of libraries used by this class


#imports of other classes in the project 
from class_one import ClassOne
from class_two import ClassTwo

def main():
    print("Hello World!")

    cOne = ClassOne() # does not take an argument
    cTwo = ClassTwo([1,2,3])  #requires an initial argument

    cOne.addNumber(12)
    cOne.addNumber(3)
    arrayOne = cOne.getArray()
    print("Print memory variable 1")
    print(arrayOne)
    cOne.clearAray()
    arrayTwo = cOne.getArray()
    print("Print memory variable 1")
    print(arrayOne) 
    print("Print memory variable 2")
    print(arrayTwo) #this is after the 'clear' call

    cTwo.addNumber(12)
    cTwo.addNumber(3)
    arrayOne = cTwo.getArray()
    print("Print memory variable 1")
    print(arrayOne)
    cTwo.clearAray()
    arrayTwo = cTwo.getArray()
    print("Print memory variable 1")
    print(arrayOne) 
    print("Print memory variable 2")
    print(arrayTwo) #this is after the 'clear' call





if __name__ == "__main__":
    main()

