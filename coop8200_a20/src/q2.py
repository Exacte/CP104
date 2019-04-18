"""
-------------------------------------------------------
[filename].py
[description of main program]
-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2014-12-03
-------------------------------------------------------
"""
MONTHS = [31, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def days_in_a_month(year):
    """
    -------------------------------------------------------
    calculates the number of days in every month for a year
    -------------------------------------------------------
    Preconditions:
       year - a year
    Postconditions:
       returns:
       MONTH - a list of the amount of every day in every month for a given year
    -------------------------------------------------------
    """
    
    test = year%4
    
    if test == 0:
        MONTHS.insert(1, 29)
    else:
        test = year%400
        if test == 0:
            MONTHS.insert(1, 29)
        else:
            MONTHS.insert(1, 28)
    return MONTHS
"""
-------------------------------------------------------
Main Program
-------------------------------------------------------
"""
year = int(input("Enter a year: "))
print(days_in_a_month(year))