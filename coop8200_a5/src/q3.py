"""
-------------------------------------------------------
primary colour product.
to prompt the user for to primary colour then giver the result of mixing them.
-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2014-09-19
------------
"""

colour1 = input("Enter a primary colour: ")
colour2 = input("Enter another primary colour: ")

if (colour1 == "red" or colour1 == "blue" or colour1 == "yellow") and (colour2 == "red" or colour2 == "blue" or colour2 == "yellow"):
    if colour1 == colour2:
        print("You can't enter the same colour twice!!!!!!")
    else:
        if (colour1 == "red" and colour2 == "blue") or (colour1 == "blue" and colour2 == "red"):
            print("Purple!!")
        elif (colour1 == "red" and colour2 == "yellow") or (colour1 == "yellow" and colour2 == "red"):
            print("Orange!!")
        else:
            print("Green")
else:
    print("You didn't enter a primary color!!!")