"""
-------------------------------------------------------

-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2014-09-19
------------
"""

bulb = int(input("Enter the wattage of the light bulb: "))
if bulb == 15:
    print("The Brightness is 125")
elif bulb == 25:
    print("The Brightness is 215")
elif bulb == 40:
    print("The Brightness is 500")
elif bulb == 60:
    print("The Brightness is 880")
elif bulb == 75:
    print("The Brightness is 1000")
elif bulb == 100:
    print("The Brightness is 1675")
else:
    print("Error: Invalid wattage")
    