"""
-------------------------------------------------------
[filename].py
[description of main program]
-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2014-11-11
-------------------------------------------------------
"""

def make_list(numb):
    """
    -------------------------------------------------------
    creates a list
    -------------------------------------------------------
    Preconditions:
       numb - the number of integers to be entered into the list
    Postconditions:
       returns:
       intList - a list containing integers
    -------------------------------------------------------
    """
    intList = []
    count = 0
    while count < numb:
        inter = input("Enter a integer: ")
        intList.append(inter)
        count += 1
    return intList

def print_list(theList):
    """
    -------------------------------------------------------
    prints a list
    -------------------------------------------------------
    Preconditions:
       theList - a list of integers
    Postconditions:
       prints:
       [return value name - return value description (return value type)] 
    -------------------------------------------------------
    """
    str = ""
    for x in theList:
        str = str + x + " "
    print(str)
"""
-------------------------------------------------------
Main Program
-------------------------------------------------------
"""
numb = int(input("Enter the number of integers to be entered: "))
print_list(make_list(numb))
