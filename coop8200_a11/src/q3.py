"""
-------------------------------------------------------
[filename].py
[description of main program]
-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2014-10-29
-------------------------------------------------------
"""

def ontarioEnv(beerServings):
    """
    -------------------------------------------------------
    calculates ontario environmental tax
    -------------------------------------------------------
    Preconditions:
       beerServings - the beer serving size
    Postconditions:
       returns:
       tax - the ontario environmental tax
    -------------------------------------------------------
    """
    if beerServings%355 == 0:
        tax = 8.93*(beerServings/355)
    elif beerServings%473 == 0:
        tax = 8.93*(beerServings/473)
    else:
        tax = 0
    return tax
    
def ontarioVol(beerManufacturer,beerServings):
    """
    -------------------------------------------------------
    calculates ontario volume tax
    -------------------------------------------------------
    Preconditions:
       beerManufacturer - the beer manufacturer
       beerServings - the beer serving size
    Postconditions:
       returns:
       volumeTax - the ontario volume tax
    -------------------------------------------------------
    """
    if beerManufacturer.lower == "P":
        volumeTax = 0
    else:
        volumeTax = .176*beerServings
    return volumeTax
        
def ontarioBasic(beerManufacturer,beerServings,beerType):
    """
    -------------------------------------------------------
    calcultaes the ontario basic tax
    -------------------------------------------------------
    Preconditions:
       beerManufacturer - the beer manufacturer
       beerServings - the beer serving size
       beerType- The beer type
    Postconditions:
       returns:
       tax - the ontario basic tax
    -------------------------------------------------------
    """
    tax = 0
    if beerManufacturer.lower == "B":
        if beerType.lower == "D":
            tax = (beerServings/1000)*.5920
        elif beerType.lower == "B" or beerType == "C":
            tax = ((beerServings/1000)*.7542)+ontarioEnv(beerServings)
    elif beerManufacturer.lower == "M":
        if beerType.lower == "D":
            tax = (beerServings/1000)*.2271
        elif beerType.lower == "B" or beerType.lower == "C":
            tax = ((beerServings/1000)*.2543)+ontarioEnv(beerServings)
    elif beerManufacturer.lower == "P":
        if beerType.lower == "D":
            tax = (beerServings/1000)*.2260
    return tax
"""
-------------------------------------------------------
Main Program
-------------------------------------------------------
"""
beerType = input("Enter the type of beer (D = draft, B = bottle, C = can): ")
beerServings = int(input("Enter the serving size(ml): "))
beerManufacturer = input("Enter a manufacturer(B=beer manufacturers, M=Microbrewers, P=Brew Pubs): ")
finalTax = ontarioBasic(beerManufacturer, beerServings, beerType)+ontarioVol(beerManufacturer, beerServings)
print("The total tax is {:.2f} cents.".format(finalTax))