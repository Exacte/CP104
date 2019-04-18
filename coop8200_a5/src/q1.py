"""
-------------------------------------------------------
First Time Home Buyer Tax Credit
To prompt the user to see if they are eligable for the First Time Home Buyer Tax Credit
-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2014-09-19
------------
"""

houseCost = input("Does your house cost less then $400,000(Y/N)? ")
combinedIncome = input("Is your combined income under $225,000(Y/N)? ")
primaryResidence = input("Have you owned a primary residence in the last three years(Y/N)? ")

if (houseCost == "y" or houseCost == "Y") and (combinedIncome == "Y" or combinedIncome == "y") and (primaryResidence == "y" or primaryResidence == "Y"):
    print("You are eligable for the First Time Home Buyer Tax Credit!")
else:
    print("You are eligable NOT for the First Time Home Buyer Tax Credit!")