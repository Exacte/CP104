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
"""
-------------------------------------------------------
Main Program
-------------------------------------------------------
"""
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
list_print(generate_list(rows, cols))
