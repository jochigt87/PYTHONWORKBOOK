#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# If Statement Exercises.

# Exercise 37: Name that Shape.

"""
Write a program that determines the name of a shape from its number of sides.
Read the number of sides from the user and then report the appropiate name as
part of a meaningful message. Your program should support shapes with anywhere
from 3 import up to (and including) 10 sides. if a number of sides outside of
this range is entered then your program should display an appropiate error
message.
"""

number_sides = input("Insert a number of sides: ")

if number_sides == "3":
    print("Triangle")
elif number_sides == "4":
    print("Quadrilateral")
elif number_sides == "5":
    print("Pentagon")
elif number_sides == "6":
    print("Hexagon")
elif number_sides == "7":
    print("Heptagon")
elif number_sides == "8":
    print("Octagon")
elif number_sides == "9":
    print("Nonagon")
elif number_sides == "10":
    print("Decagon")
else:
    print("That number of sides is out of range")
