"""
-------------------------------------------------------
Random numbers
takes a range from the user and the amount of generated numbers,
then outputs the amount of negative numbers, positive numbers and zeros.
-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2014-09-19
------------
"""
import random
countZero = 0
countNegative = 0
countPositive = 0
total = 0
i = 0
ranges = int(input("Enter the max range: "))
numbers = int(input("Enter the amount of numbers to be generated: "))
while i < numbers:
    randomNumber = random.randint(-ranges,ranges)
    if randomNumber == 0:
        countZero += 1
    elif randomNumber < 0:
        countNegative += 1
    else:
        countPositive += 1
    total = total + randomNumber
    i += 1
average = total/numbers
print("Number of positive values: {}".format(countPositive))
print("Number of negative values: {}".format(countNegative))
print("Number of zeros: {}".format(countZero))
print("Average: {:.2f}".format(average))