"""
-------------------------------------------------------
[filename].py
[description of main program]
-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2014-11-07
-------------------------------------------------------
"""

def plural(noun):
    """
    -------------------------------------------------------
    given a word, turns it into its plural form
    -------------------------------------------------------
    Preconditions:
       noun - a noun
    Postconditions:
       prints:
       noun - returns a string which is a plural version of the entered noun
    -------------------------------------------------------
    """
    noun = noun.lower()
    if noun.endswith("ay") == False and noun.endswith("ey") == False and noun.endswith("oy") == False and noun.endswith("y") == True:
        y = noun[-1]
        x = noun.rfind(y)
        noun = noun[0:x] + "ies"
    elif noun.endswith("ch") == True or noun.endswith("sh") == True:
        noun = noun + "es"
    elif noun.endswith("s") == True:
        noun = noun + "es"
    else:
        noun = noun + "s"
    print(noun)

"""
-------------------------------------------------------
Main Program
-------------------------------------------------------
"""
noun = input("Enter a noun: ")
plural(noun)
