"""
-------------------------------------------------------
Béchamel sauce
Takes the desired amount of servings and adjust recipe.
-------------------------------------------------------
Author:  Mason Cooper
ID:      140328200
Email:   coop8200@mylaurier.ca
Version: 2014-09-19
------------
"""

Milk = 4/6
Butter = 8/6
Flour = .5/6
Salt = 2/6

servings = float(input("What is your desired serving? "))

Milk = Milk*servings
Butter = Butter*servings
Flour = Flour*servings
Salt = Salt*servings

print("{:.1f} Cups of milk".format(Milk))
print("{:.1f} Tablespoons of unsalted butter".format(Butter))
print("{:.1f} Cups of all purpose flour".format(Flour))
print("{:.1f} Table spoons of kosher salt".format(Salt))