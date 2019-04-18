"""
-------------------------------------------------------
pennyweight
converts pennyweight to grams
-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2014-09-19
------------
"""

PENNYWEIGHT = 1.5552

rangeStart = int(input("Enter a the start of the range: "))
rangeEnd = int(input("Enter a the end of the range: "))
for i in range(rangeStart,(rangeEnd+1)):
    grams = i*PENNYWEIGHT
    print("{:.2f}".format(grams))