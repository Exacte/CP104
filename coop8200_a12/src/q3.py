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

def find(sentence, sub):
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
    print(sentence.find(sub))

"""
-------------------------------------------------------
Main Program
-------------------------------------------------------
"""
sentence = input("Enter a sentence: ")
sub = input("Enter a substring: ")
find(sentence, sub)
while True:
    cont = input("Would you like to continue(Y/N)? ")
    cont = cont.upper()
    if cont == "Y":
        sentence = input("Enter a sentence: ")
        sub = input("Enter a substring: ")
        find(sentence, sub)
    elif cont == "N":
        print("End")
        break