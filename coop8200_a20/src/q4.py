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
MONTHSNUMB = [31, [28, 29], 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DAY = 1
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

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
       h - a number representing a day of the week
    -------------------------------------------------------
    """
    j = int(year[0:2])
    k = int(year[2:4])
    h = (q+((26*(m+1))//10)+k+(k//4)+(j//4)+5*j)%7
    return h

def days_in_a_month(month, year):
    """
    -------------------------------------------------------
    calculates the number of days in a month
    -------------------------------------------------------
    Preconditions:
       month - a month in a given year
       year - a year
    Postconditions:
       returns:
       days - the number of days in a given month
    -------------------------------------------------------
    """
    test = year%4
    
    if test == 0:
        if month == 2:
            days = MONTHSNUMB[1][1]
        else:
            days = MONTHSNUMB[month-1]
    else:
        test = year%400
        if test == 0:
            if month == 2:
                days = MONTHSNUMB[1][1]
            else:
                days = MONTHSNUMB[month-1]
        else:
            if month == 2:
                days = MONTHSNUMB[1][0]
            else:
                days = MONTHSNUMB[month-1]
    return days

def calender(numb, h, month, year):
    """
    -------------------------------------------------------
    [function description]
    -------------------------------------------------------
    Preconditions:
       [parameter name - parameter description (parameter type and constraints)]
    Postconditions:
       [returns: or prints:]
       [return value name - return value description (return value type)] 
    -------------------------------------------------------
    """
    calenderList = []
    for i in range(1,numb+1):
        calenderList.append(i)
    
    if h == 0:
            for i in range(6):
                calenderList.insert(0, ' ')
    else: 
        for x in range(h):
                calenderList.insert(0, ' ')
    
    month = MONTHS[month-1]
    
    print("{:>13} {:13}".format(month, year))
    print()
    print("{} {} {} {} {} {} {}".format("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"))
    
    for z in range(1,len(calenderList)):
        print("{:3} ".format(calenderList[z]), end= "")
        if z%7 == 0:
            print()
    
    
"""
-------------------------------------------------------
Main Program
-------------------------------------------------------
"""
year = input("Enter a year: ")
month = int(input("Enter a month(1-12): "))
x = day_of_the_week(DAY, month, year)
numb = days_in_a_month(month, int(year))
print()
calender(numb, x, month, year)