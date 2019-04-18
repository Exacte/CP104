"""
-------------------------------------------------------

-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2014-09-19
------------
"""
WEEK = 7
averageDefects = 0
totalDefects = 0
maxNumber = 0
for i in range(1,8):
    defects = int(input("Enter the number of defects on {} day: ".format(i)))
    if maxNumber <= defects:
        maxNumber = defects
    totalDefects = totalDefects + defects
averageDefects = totalDefects/WEEK
print("Your average number of defects per day for the 7 day week is: {:.2f}".format(averageDefects))
print("The Higst amount of defects a day was {}".format(maxNumber))