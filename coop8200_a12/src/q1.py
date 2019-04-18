"""
-------------------------------------------------------
[filename].py
[description of main program]
-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2014-11-04
-------------------------------------------------------
"""

def digit(numb):
    """
    -------------------------------------------------------
    [function description]
    -------------------------------------------------------
    Preconditions:
       [parameter name - parameter description (parameter type and constraints)]
    Postconditions:
       [returns: or prints:]
       [return value name - return value description (return value type)] 
    -------------------------------------------------------
    """
    print(numb.isdigit())
    
"""
-------------------------------------------------------
Main Program
-------------------------------------------------------
"""
numbers = input("Enter a string: ")
digit(numbers)
while True:
    cont = input("Would you like to continue(Y/N)? ")
    cont = cont.upper()
    if cont == "Y":
        numbers = input("Enter a string: ")
        digit(numbers)
    elif cont == "N":
        print("End")
        break
