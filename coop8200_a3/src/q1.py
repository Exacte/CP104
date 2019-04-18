"""
-------------------------------------------------------
Area of a Cylinder
To calculate the area of a cylinder
-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2014-09-19
-------------------------------------------------------
"""

Pi = 3.14

cylinderHeight = float(input("What is the Height of the cylinder(m)? "))
cylinderRadius = float(input("What is the radius of the cylinder(m)? "))

baseArea = Pi*(cylinderRadius**2)
volume = baseArea*cylinderHeight

print("The base are is {0:.2f} and the volume is {1:.2f}.".format(baseArea, volume))