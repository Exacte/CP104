"""
-------------------------------------------------------
[filename].py
[description of main program]
-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2014-11-19
-------------------------------------------------------
"""
import os

def average_percip_temp(f1, f2, fO):
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
    string = ""
    hold = ""
    counter = 0
    f1.seek(0)
    line1 = f1.readline()
    while line1 != "":
        counter += 1
        line1 = f1.readline()
    f1.seek(0)
    for i in range(0,counter):
        line1 = f1.readline()
        line1 = line1.split()
        
        line2 = f2.readline()
        line2 = line2.split()
        for i in range(len(line2)):
            hold = "{} ".format(line2[i])
        string = ("{} {} {}".format(line1[0], hold, line1[1]))
        print(string, file = fO, end= "\n")
        print("Complete!")
        
"""
-------------------------------------------------------
Main Program
-------------------------------------------------------
"""
fileF = input("Enter the first input file name: ")
fileS = input("Enter the second input file name: ")
fileO = input("Enter the output file name: ")
if os.path.exists(fileO) == False:
    ask = input("Output file D.N.E, would you like to create a new one(Y/N)? ")
    ask = ask.upper()
    if ask == "Y":
        if os.path.exists(fileF) == True and os.path.exists(fileS) == True:
            f1 = open(fileF, "r", encoding="utf-8")
            f2 = open(fileS, "r", encoding="utf-8")
            fO = open(fileO, "w+", encoding="utf-8")
            average_percip_temp(f1, f2, fO)
            f1.close()
            f2.close()
            fO.close()
        else:
            print("Input File's Does Not Exist")
    else:
        print("Error")
else:
    if os.path.exists(fileF) == True and os.path.exists(fileS) == True:
            f1 = open(fileF, "r", encoding="utf-8")
            f2 = open(fileS, "r", encoding="utf-8")
            fO = open(fileO, "w+", encoding="utf-8")
            average_percip_temp(f1, f2, fO)
            f1.close()
            f2.close()
            fO.close()
