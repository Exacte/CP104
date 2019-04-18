"""
-------------------------------------------------------
Initial deposit
calculates the initial amount to be deposited to reach the desired
final result.
-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2014-09-19
-------------------------------------------------------
"""

finalValue = float(input("What is you desired final amount: "))
intrest = float(input("What is the annual percent? "))/100
years = float(input("How long will the money sit for(yr)? "))
months = years*12

initialDeposit = finalValue/(1 + intrest)**months

print("The initial amount to invest is {:.2f}".format(initialDeposit))