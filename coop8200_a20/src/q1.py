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
DAYS = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

def day_of_the_week(q, m, year):
    """
    -------------------------------------------------------
    calculates the day of the week for a specific date
    -------------------------------------------------------
    Preconditions:
       q - a day in a given month
       m - a month in a given year
       year - a given year
    Postconditions:
       returns:
       DAYS[] - a list of the days of the week
       h - a number representing a day of the week
    -------------------------------------------------------
    """
    j = int(year[0:2])
    k = int(year[2:4])
    h = (q+((26*(m+1))//10)+k+(k//4)+(j//4)+5*j)%7
    return DAYS[h]

"""
-------------------------------------------------------
Main Program
-------------------------------------------------------
"""
year = input("Enter a year: ")
month = int(input("Enter a month(1-12): "))
day = int(input("Enter a day(1-31): "))
print(day_of_the_week(day, month, year))