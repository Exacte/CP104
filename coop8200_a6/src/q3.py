"""
-------------------------------------------------------

-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2014-09-19
------------
"""

beerType = input("Enter the type of beer (D = draft, B = bottle, C = can): ")
beerServings = int(input("Enter the serving size(L): "))
beerManufacturer = input("Enter a manufacturer(B=beer manufacturers, M=Microbrewers, P=Brew Pubs): ")
beerServingsTax = beerServings*.176
environmentalTax = beerServingsTax/355 + .0893

if beerManufacturer == "B":
    if beerType == "D":
        tax = beerServings/1000*.5920
        print("The Beer tax is ${0:.2f} and the Ontario beer tax is {1:.2f}".format(tax,beerServingsTax))
    elif beerType == "B":
        tax = beerServings/1000*.7542
        print("The Beer tax is ${0:.2f} and the Ontario beer tax is {1:.2f}".format(tax,beerServings))
    elif beerType == "C":
        tax = beerServings/1000*.7542
        print("The Beer tax is ${0:.2f} and the Ontario beer tax is {1:.2f}".format(tax,environmentalTax))
    else:
        print("Invalid input")
        
elif beerManufacturer == "M":
    if beerType == "D":
        tax = beerServings/1000*.2271
        print("The Beer tax is ${0:.2f} and the Ontario beer tax is {1:.2f}".format(tax,beerServingsTax))
    elif beerType == "B":
        tax = beerServings/1000*.2543
        print("The Beer tax is ${0:.2f} and the Ontario beer tax is {1:.2f}".format(tax,beerServingsTax))
    elif beerType == "C":
        tax = beerServings/1000*.2543
        print("The Beer tax is ${0:.2f} and the Ontario beer tax is {1:.2f}".format(tax,environmentalTax))
    else:
        print("Invalid input")

elif beerManufacturer == "P":
    if beerType == "D":
        tax = beerServings/1000*.2260
        print("The Beer tax is ${:.2f}".format(tax))
    else:
        print("Invalid input")

else:
    print("Invalid input")