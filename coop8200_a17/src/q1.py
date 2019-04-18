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
def count_lines(f):
    """
    -------------------------------------------------------
    Counter
    -------------------------------------------------------
    Preconditions:
       f - a file
    Postconditions:
       returns:
       counter - the number of lines in a file
    -------------------------------------------------------
    """
    counter = 0
    line = f.readline()
    while line != "":
        counter+=1
        line = f.readline()
    counter -= 1
    return counter

def clean_up(f, counter, ask, fO, missing):
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
    hold = 0
    f.seek(0)
    line = f.readline()
    line = line.split(",")
    if (ask in line) == True:
        for x in range(len(line)):
            if ask == line[x]:
                hold = x
        for i in range(0,counter):
            line = f.readline()
            line = line.split(",")
            if line[hold] == missing:
                line = f.readline()
            for z in range(len(line)):
                print("{},".format(line[z]), file = fO, end= "")
            print("", file = fO, end = "")          
    else:
        print("Error!")
    print("Complete!")
"""
-------------------------------------------------------
Main Program
-------------------------------------------------------
"""
print("""Animal
Weight
Brain_weight
Nondreaming
Dreaming
Sleep_hours
Life_span
Gestation
Predation_index
Exposure
Danger""")
print()

ask = input("Which of the above Row's would you like Cleaned up? ")
fileS = input("Enter the input file name: ")
fileO = input("Enter the output file name: ")
missing = int(input("What represents a missing value? "))

if os.path.exists(fileO) == False:
    ask = input("Output file D.N.E, would you like to create a new one(Y/N)? ")
    ask = ask.upper()
    if ask == "Y":
        if os.path.exists(fileS) == True:
            f = open(fileS, "r", encoding="utf-8")
            fO = open(fileO, "w", encoding="utf-8")
            count = count_lines(f)
            clean_up(f, count, ask, fO, missing)
            f.close()
            fO.close()
        else:
            print("Input File's Does Not Exist")
    else:
        print("Error")
else:
    if os.path.exists(fileS) == True:
            f = open(fileS, "r", encoding="utf-8")
            fO = open(fileO, "w", encoding="utf-8")
            count = count_lines(f)
            clean_up(f, count, ask, fO, missing)
            f.close()
            fO.close()