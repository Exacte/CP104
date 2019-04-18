"""
-------------------------------------------------------
[program name]
[program description]
-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2014-09-19
-------------------------------------------------------
"""

Tax = .13

item1 = float(input("How much does your first item cost? "))
item2 = float(input("How much does your second item cost? "))
item3 = float(input("How much does your third item cost? "))

totalCost = item1 + item2 + item3
salesTax = totalCost*Tax
totalWithTax = totalCost + salesTax

print("Total cost without tax: " + str(totalCost))
print("Sales tax is: {:.2f}".format(salesTax))
print("Your total with tax: {:.2f}".format(totalWithTax))