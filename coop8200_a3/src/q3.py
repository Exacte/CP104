"""
-------------------------------------------------------
Total cost
takes the cost of a meal and outputs the tax, the tip
and the final tax.
-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2014-09-19
-------------------------------------------------------
"""

OntarioTax = .13
WesternTax = .05
Tip = .15

mealCost = float(input("What was the cost of the meal? "))
province = str(input("Are you in Ontario (Y/N)"))
if province == "y" or province == "Y":
    tax = mealCost*OntarioTax
    tip = (mealCost + tax)*Tip
    finalCost = mealCost + tax + tip
    print("Cost of the meal:")
    print("{0:>12s}{1: >5.2f}".format("Food: $ ", mealCost))
    print("{0:>12s}{1: >5.2f}".format("Tax: $ ", tax))
    print("{0:>12s}{1: >5.2f}".format("Tip: $ ", tip))
    print("-------------------")
    print("{0:<11s}{1: >6.2f}".format("Total: $ ", finalCost))
    
elif province == "N" or province == "n":
    tax = mealCost*WesternTax
    tip = (mealCost + tax)*Tip
    finalCost = mealCost + tax + tip
    print("Cost of the meal:")
    print("{0:>12s}{1: >5.2f}".format("Food: $ ", mealCost))
    print("{0:>12s}{1: >5.2f}".format("Tax: $ ", tax))
    print("{0:>12s}{1: >5.2f}".format("Tip: $ ", tip))
    print("-------------------")
    print("{0:<11s}{1: >6.2f}".format("Total: $ ", finalCost))
    
else:
    print("Invalid input!")