"""
-------------------------------------------------------
[filename].py
[description of main program]
-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2014-11-21
-------------------------------------------------------
"""
import os

def average_sleep(max, min, f):
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
    counting = 0
    total = 0
    line = f.readline()
    line = line.split(",")
    while line != "":
        if float(line[1]) > min and float(line[5]) < max:
            total += float(line[5])
        counting += 1
        line = f.readline()
        line = line.split(",")
    average = total/counting
    print("Average for Weight range {}-{}: {:.2f}".format(min, max, average))

"""
-------------------------------------------------------
Main Program
-------------------------------------------------------
"""

max = int(input("Enter a max weight range: "))
min = int(input("Enter a min weight range: "))
file = input("Enter the input file: ")

if os.path.exists(file) == True:
        f = open(file, "r", encoding="utf-8")
        average_sleep(max, min, f)
        f.close()
else:
    print("Input File's Does Not Exist")