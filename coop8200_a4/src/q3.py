"""
-------------------------------------------------------

-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2014-09-19
------------
"""

amountData = float(input("How much data will be transmitted(GB)? "))
fastestSpeed = float(input("What is your fastest download speed(Mbps)? "))
slowestSpeed = float(input("What is your slowest download speed(Mbps)? "))

amountData = (amountData*8000)
fastestTime = (amountData/fastestSpeed)/60
slowestTime = (amountData/slowestSpeed)/60

print("The fastest the movie will download is {0:.2f} minutes. The slowest it will download is {1:.2f} minutes!".format(fastestTime, slowestTime))
