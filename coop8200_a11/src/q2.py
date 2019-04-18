"""
-------------------------------------------------------
[filename].py
[description of main program]
-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2014-10-29
-------------------------------------------------------
"""
import random

def get_random(max_range):
    """
    -------------------------------------------------------
    creates a random number
    -------------------------------------------------------
    Preconditions:
       max_range - the range at which the function creates a random number
    Postconditions:
       returns:
            number - a random number
    -------------------------------------------------------
    """
    number = random.randint(-max_range,max_range+1)
    return number

def classify(number):
    """
    -------------------------------------------------------
    classifies a number as positive, negative or zero
    -------------------------------------------------------
    Preconditions:
       number - a number
    Postconditions:
        returns:
       p - a positive number
       n - a negative number
       or
       z - a zero
    -------------------------------------------------------
    """
    p = 1
    n = -1
    z = 0
    if number > 0:
        return p
    elif number < 0:
        return n
    else:
        return z
    
def count(max_range, generated):
    """
    -------------------------------------------------------
    counts the number of positive, negative and zeros generated
    -------------------------------------------------------
    Preconditions:
       generated - the amount of random numbers to be generated
       the range at which the function creates a random number
    Postconditions:
       prints:
       countP - the number of positive numbers
       countN- the number of negative numbers
       CountZ - the number of zeros
    -------------------------------------------------------
    """
    countP = 0
    countN = 0
    countZ = 0
    while generated > 0:
        classify(get_random(max_range))
        if classify(get_random(max_range)) == 1:
            countP += 1
        elif classify(get_random(max_range)) == -1:
            countN += 1
        else:
            countZ += 1
        generated -= 1
    print("Number of positive numbers generated was: {}".format(countP))
    print("Number of negative numbers generated was: {}".format(countN))
    print("Number of zero's generated was: {}".format(countZ))
        
"""
-------------------------------------------------------
Main Program
-------------------------------------------------------
"""
maximum = int(input("Enter the max range. "))
generated = int(input("Enter the amount of numbers to be generated. "))
count(maximum, generated)
