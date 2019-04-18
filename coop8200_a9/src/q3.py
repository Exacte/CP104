"""
-------------------------------------------------------
sum of squares continuing
calculates the sum of squares until user prompts the program to stop
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
while True:
    while count < n+1:
        totalvalue = totalvalue + (count**2)
        count += 1
    print("The sum of squares is {}".format(totalvalue))
    ask = input("Would you like to run the program again(Y/N)? ")
    if ask == "Y" or ask == "y":
        n = int(input("Enter the value of n: "))
    else:
        print("Finished.")
        break