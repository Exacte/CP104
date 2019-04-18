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

def startswith(sentence, sub):
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
    print(sentence.startswith(sub))

"""
-------------------------------------------------------
Main Program
-------------------------------------------------------
"""
sentence = input("Enter a sentence: ")
sub = input("Enter a substring: ")
startswith(sentence, sub)
while True:
    cont = input("Would you like to continue(Y/N)? ")
    cont = cont.upper()
    if cont == "Y":
        sentence = input("Enter a sentence: ")
        sub = input("Enter a substring: ")
        startswith(sentence, sub)
    elif cont == "N":
        print("End")
        break
