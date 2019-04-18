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

def file_average(f):
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
    average = 0
    f.seek(0)
    print("Average:")
    line = f.readline().strip()
    while line != "":
        line = line.split(",")
        for i in range(len(line[1:])):
            average += float(line[1])/int(len(line[1:]))
        print("{}- {:.2f}".format(line[0], average))
        line = f.readline().strip()
    return
    
"""
-------------------------------------------------------
Main Program
-------------------------------------------------------
"""
file = input("Enter the file name: ")
if os.path.exists(file) == True:
    f = open(file, "a+", encoding="utf-8")
    file_average(f)
    f.close()
else:
    print("File Does Not Exist")