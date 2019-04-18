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
import random

def ir():
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
    deck = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    return deck
def dealt(deck, numb):
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
    random.shuffle(deck)
    x = 0
    hand = []
    while x < numb:
        hand.insert(x, deck[x])
        x += 1
    return hand

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
    r = ""
    for x in theList:
        r = r + x + " "
    return r
"""
-------------------------------------------------------
Main Program
-------------------------------------------------------
"""
numb = int(input("Enter the number of cards to be dealt: "))
print(print_list(dealt(ir(), numb)))