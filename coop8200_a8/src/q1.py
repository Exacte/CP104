"""
-------------------------------------------------------
Percipetation
calculates the total and average amount of percipitation over a period of years
-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2014-09-19
------------
"""

percipTotal= 0
percipAverage = 0
years = int(input("Enter the amount of years. "))
print("Enter precipitation in mm. ")
for i in range(1,years+1):
    print("Year {}".format(i))
    percipJa = float(input("January- "))
    percipF = float(input("February- "))
    percipM = float(input("March- "))
    percipA = float(input("April- "))
    percipMa = float(input("May- "))
    percipJ = float(input("June- "))
    percipJu = float(input("July- "))
    percipAu = float(input("August- "))
    percipS = float(input("September- "))
    percipO = float(input("October- "))
    percipN = float(input("November- "))
    percipD = float(input("December- "))
    percipTotal = percipTotal+percipJa+percipF+percipM+percipA+percipMa+percipJ+percipJu+percipAu+percipS+percipO+percipN+percipD
    percipAverage = percipTotal/12/years
numberOfMonths = years*12
print("Number of months: {}".format(numberOfMonths))
print("Total: {}".format(percipTotal))
print("Average: {:.1f}".format(percipAverage))