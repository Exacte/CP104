"""
-------------------------------------------------------
[filename].py
[description of main program]
-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2014-11-08
-------------------------------------------------------
"""
def initial(name):
    """
    -------------------------------------------------------
    takes a name of a person and returns the initials.
    -------------------------------------------------------
    Preconditions:
       name - a persons name
    Postconditions:
       prints:
       first - the persons first initial
       middle - the persons middle initial
       last - the persons last initial
    -------------------------------------------------------
    """
    name = name.upper()
    first = name[0:name.find(" ")]
    last = name[name.rfind(" "):]
    middle = ""
    if name.count(" ") == 2:
        middle = name[name.find(" "):name.rfind(" ")]
        middle = middle.lstrip()
        middle = "{}.".format(middle[0])
        count += 1
    last = last.lstrip()
    print("{}.{}{}".format(first[0], middle,last[0]))

"""
-------------------------------------------------------
Main Program
-------------------------------------------------------
"""
name = input("Enter your full name: ")
initial(name)
