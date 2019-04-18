"""
-------------------------------------------------------

-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2014-09-19
------------
"""
CANOEING = 3.5068
HIKING = 6.0
ROLLERBLADING = 7.5068
TAEKWONDO = 10.3014
TAICHI = 3.0
HOUR = 60
mass = float(input("Enter your weight: "))
for time in range(15,91,15):
    caloriesBurned = (time/HOUR)*(mass/CANOEING)
    print("{:<14}{}".format("Activites",time))
    print("{:<14}{:.2f}".format("Canoeing",caloriesBurned))
    caloriesBurned = (time/HOUR)*(mass/HIKING)
    print("{:<14}{:.2f}".format("Hiking",caloriesBurned))
    caloriesBurned = (time/HOUR)*(mass/ROLLERBLADING)
    print("{:<14}{:.2f}".format("Rollerblading",caloriesBurned))
    caloriesBurned = (time/HOUR)*(mass/TAEKWONDO)
    print("{:<14}{:.2f}".format("Tae kwon do",caloriesBurned))
    caloriesBurned = (time/HOUR)*(mass/TAICHI)
    print("{:<14}{:.2f}".format("Tai chi",caloriesBurned))
    print("")
