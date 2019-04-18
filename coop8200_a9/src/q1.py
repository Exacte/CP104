"""
-------------------------------------------------------
sum of squares
calculates the sum of suares
-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2014-09-19
------------
"""

totalvalue = 0
count = 0
n = int(input("Enter the value of n: "))
while count < n+1:
    totalvalue = totalvalue + (count**2)
    count += 1
print("The sum of squares is {}".format(totalvalue))