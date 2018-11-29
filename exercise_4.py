#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Introduction to Programming Exercises.

# Exercise :Area of a Field.

"""
Create a program that reads the lenght and width of a farmer's field from the
user in feet. Display the area of the field in acres.

Hint: There are 43,560 square feet in an acre.
"""

ACRE = 43560.04

lenght = float(input("Insert the lenght in feets: "))
width = float(input("Insert the width square feets: "))
total = (lenght * width) * 0.0000229568411387

print(total, "Acres")
