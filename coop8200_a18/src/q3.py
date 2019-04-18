"""
-------------------------------------------------------
[filename].py
[description of main program]
-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2014-11-24
-------------------------------------------------------
"""
EMPTY = "."
FILLED = "Z"

def generate_list(row, col):
    """
    -------------------------------------------------------
    generates a list
    -------------------------------------------------------
    Preconditions:
       row - the number of rows in a 2d list
       col - the number of columns in a 2d list
    Postconditions:
       returns:
       matrix - a 2d list
    -------------------------------------------------------
    """
    matrix = [[EMPTY]*col]*row
    return matrix

def list_print(matrix):
    """
    -------------------------------------------------------
    prints a 2d list
    -------------------------------------------------------
    Preconditions:
       matrix - a 2d list
    Postconditions:
    -------------------------------------------------------
    """
    for i in range(len(matrix)):
        for x in range(len(matrix[i])):
            print(matrix[i][x], end= "")
        print()
        
def list_boarder(matrix):
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
    hold = []
    for i in range(len(matrix[0])):
        hold.append(FILLED)
    del matrix[0]
    matrix.insert(0, hold)
    del matrix[-1]
    matrix.insert(len(matrix), hold)
    
    for x in range(1, len(matrix)-1):
        matrix[x].pop(0)
        matrix[x].insert(0, FILLED)
        matrix[x].pop(-1)
        matrix[x].insert(len(matrix[x]), FILLED)
    
    return matrix
        
"""
-------------------------------------------------------
Main Program
-------------------------------------------------------
"""
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
list_print(list_boarder(generate_list(rows, cols)))