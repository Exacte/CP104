"""
-------------------------------------------------------

-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2014-09-19
------------
"""

resRate = int(input("Enter the breaths per minute: "))
age = int(input("Enter the age(years): "))

if age == 0:
    if (resRate >= 25) and (resRate <= 60):
        print("your average respiration rate is within the acceptable range.")
    elif (resRate < 25):
        print("Your average respiration rate is to LOW!!")
    else:
        print("Your average respiration rate is to HIGH!")
elif (age >= 1) and (age <= 4):
    if (resRate >= 20) and (resRate <= 30):
        print("your average respiration rate is within the acceptable range.")
    elif (resRate < 20):
        print("Your average respiration rate is to LOW!!")
    else:
        print("Your average respiration rate is to HIGH!")
elif (age >= 5) and (age <= 14):
    if (resRate >= 15) and (resRate <= 25):
        print("your average respiration rate is within the acceptable range.")
    elif (resRate < 15):
        print("Your average respiration rate is to LOW!!")
    else:
        print("Your average respiration rate is to HIGH!")
elif (age >= 15) and (age <= 18):
    if (resRate >= 11) and (resRate <= 23):
        print("your average respiration rate is within the acceptable range.")
    elif (resRate < 23):
        print("Your average respiration rate is to LOW!!")
    else:
        print("Your average respiration rate is to HIGH!")
else:
    print("Your to old!")