#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Introduction to Programming Exercises.

# Exercise 14: Height Units.

"""
Many people think about their height in feet and inches, even in some
countries that primarily use the metric system. Write a program that reads a
number of feet from the user, followed by a number of inches. Once these
values are read, your program should compute and display the equivalent number
of centimeters.

    👉 Hint: One foot is 12 inches. One inch is 2.54 centimeters.
"""

ONE_FOOT = 12 # Inches
ONE_INCH = 2.54 # Centimeters

feets = float(input("Insert the amount of feets: "))
inches = float(input("Insert the amount of inches:"))

total_centimeters = (feets * ONE_FOOT + inches) * ONE_INCH
print(total_centimeters)
