"""
-------------------------------------------------------
[filename].py
[description of main program]
-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2014-11-08
-------------------------------------------------------
"""
def prefix_length(string, sub):
    """
    -------------------------------------------------------
    given two words returns the longest common prefix between them
    -------------------------------------------------------
    Preconditions:
       string - a word
       sub - a word
    Postconditions:
       prints:
       sub - the longest prefix between the two words
    -------------------------------------------------------
    """
    count = 0
    while True:
        check = string[0:count]
        if sub.startswith(check) == True:
            count += 1
        else:
            break
    print(sub[0:count-1])
    
"""
-------------------------------------------------------
Main Program
-------------------------------------------------------
"""
word1 = input("Enter a word: ")
word2 = input("Enter a second word: ")
prefix_length(word1, word2)
