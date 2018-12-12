#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Introduction to Programming Exercises.

# Exercise 30: Units of Pressure.

"""
In this exercise you will create a program that reads a pressure from the user
in kilopascals. Once the pressure has been read your program should report
the equivalent pressure in pounds per square inch, millimeters of mercury and
atmospheres. Use your research skills to determine the conversion factors
between these units.
"""
kilopascals = float(input("Insert the pressure in kilopascals: "))

pounds_per_inch = (0.145 * kilopascals)
mmHg = (7.5006 * kilopascals)
atmospheres = (0.0099 * kilopascals)


print(kilopascals, "kilopascals are:")
print(f'{pounds_per_inch:.2f}', "pounds per square")
print(f'{mmHg:.2f}', "millimeters of mercury")
print(f'{atmospheres:.2f}', "atmospheres")
