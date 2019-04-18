"""
-------------------------------------------------------
[filename].py
[description of main program]
-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2014-11-18
-------------------------------------------------------
"""
import os
def average_percip(f):
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
    print("   {:>10} {:>10} {:>10} {:>10} {:>10} {:>10} {:>10} {:>10} {:>10} {:>10} {:>10} {:>10}".format("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"))
    string = ""
    yearcheck = "72"
    monthcheck = "Jan"
    total = 0
    counter = 0
    averageList = []
    hold = []
    f.seek(0)
    line = f.readline()
    while line != "":
        counter += 1
        line = f.readline()
    f.seek(0)
    for i in range(0,counter):
        line = f.readline()
        line = line.split()
        line[0] = line[0].split('-')
        if len(line[0]) == 3:
            year = line[0][2]
            month = line[0][1]
            if year == yearcheck:
                if month == monthcheck:
                    total += float(line[1])
                    counter += 1
                elif month != monthcheck:
                    average = (total/counter)
                    averageList.append(average)
                    hold.extend(averageList)
                    averageList = []
                    counter = 0
                    total = 0
                    monthcheck = month
            elif year != yearcheck:
                print(yearcheck, end= "")
                for i in range(len(hold)):
                    print(" {:10.2f}".format(float(hold[i])), end= "")
                print()
                hold = []
                yearcheck = year
    print(yearcheck, end= "")
    for i in range(len(hold)):
        print(" {:>10.2f}".format(float(hold[i])), end= "")
"""
-------------------------------------------------------
Main Program
-------------------------------------------------------
"""
file = input("Enter the file name: ")
if os.path.exists(file) == True:
    f = open(file, "r", encoding="utf-8")
    average_percip(f)
    f.close()
else:
    print("File Does Not Exist")
