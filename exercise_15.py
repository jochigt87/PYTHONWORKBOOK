#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Introduction to Programming Exercises.

# Exercise 15: Distance Units.

"""
In this exercise, you will create a program that reading a measurement in feet
from the user. Then your program should display the equivalent distance in
inches, yards, and miles. Use the Internet to look up the necessary conversion
factors if you don't have them memorized.
"""

feets = float(input("Insert your measurement in feets: "))

INCHES = 12 # feets
YARDS = 0.33333333333333 # feets
MILES = 0.00018939393939394 # feets

print(f'{feets*INCHES:.2f}', "Inches")
print(f'{feets*YARDS:.2f}', "Yards")
print(f'{feets*MILES:.2f}', "Miles")
