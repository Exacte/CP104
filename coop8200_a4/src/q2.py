"""
-------------------------------------------------------

-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2014-09-19
------------
"""

song = input("Enter the name of the song: ")
views = int(input("How many views does the video have? "))
minutes = int(input("How many minutes is the video? "))
seconds = int(input("and how many seconds? "))

seconds = seconds + (minutes*60)
years = seconds/31536000

print("while watching {0}, you could have spent {1:.7f} years doing homework.".format(song, years))