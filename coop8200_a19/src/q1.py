"""
-------------------------------------------------------
[filename].py
[description of main program]
-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2014-11-27
-------------------------------------------------------
"""
import meat_data


def standard():
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
    for i in range(len(meat_data.meats)):
        if float(meat_data.meats[i][4]) != 75:
            hold = 75/meat_data.meats[i][4]
            for x in range(4, len(meat_data.meats[i])):
                hold2 = hold * float(meat_data.meats[i][x])
                del meat_data.meats[i][x]
                meat_data.meats[i].insert(x, hold2)
                
    for i in range(len(meat_data.meats)):
        for x in range(len(meat_data.meats[i])):
            print(meat_data.meats[i][x], end= "")
        print()
"""
-------------------------------------------------------
Main Program
-------------------------------------------------------
"""
standard()