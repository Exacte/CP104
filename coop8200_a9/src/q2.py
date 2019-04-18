"""
-------------------------------------------------------
sum of squares every step
calculates the sum of squares printing every step of the way
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
    print("n is {0} and the sum of squares is {1}".format(count, totalvalue))
    count += 1