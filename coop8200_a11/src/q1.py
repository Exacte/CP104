"""
-------------------------------------------------------
[filename].py
[description of main program]
-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2014-10-28
-------------------------------------------------------
"""

ABSOLUTEC = -273.15
ABSOLUTEF = -459.67

def celsius(temp):
    """
    -------------------------------------------------------
    Converts celsius to fahrenheit
    -------------------------------------------------------
    Preconditions:
       temp- tempature in fahrenheit
    Postconditions:
       prints:
       temperature in celsius
    -------------------------------------------------------
    """
    new_temp = temp*(9/5)+32
    print("{:.1f} degrees Celsius is {:.1f} degrees Farenheit.".format(temp, new_temp))

def farhenheit(temp):
    """
    -------------------------------------------------------
    Converts fahrenheit to celsius
    -------------------------------------------------------
    Preconditions:
       temp- tempature in celsius
    Postconditions:
       prints:
       temperature in fahrenheit
    -------------------------------------------------------
    """
    new_temp = (temp - 32)*(5/9)
    print("{:.1f} degrees Farenheit is {:.1f} degrees Celsius.".format(temp, new_temp))
"""
-------------------------------------------------------
Main Program
-------------------------------------------------------
"""
choice = input("What Conversion would you like to make? (F/C) ")
temp = float(input("Enter a temperature: "))
if choice.lower().startswith("f") == True:
    if temp < ABSOLUTEC:
        print("Error!")
    else:
        celsius(temp)
elif choice.lower().startswith("c") == True:
    if temp < ABSOLUTEF:
        print("Error!")
    else:
        farhenheit(temp)
elif (choice.lower().startswith("f") == False and choice.lower().startswith("c") == False):
    print("Error!")