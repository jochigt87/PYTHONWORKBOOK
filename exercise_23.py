#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Introduction to Programming Exercises.

# Exercise 23: Area of a Regular Polygon.

import math
"""
A Polygon is regular if its sides area all the same lenght and the angles
between all the adjacent sides are equal. The area of a regular polygon can be
computed using the following formula, where s is the lenght of a side and n is
the number of sides:

        area = n*s^2 / 4 * tan(pi/n)

Write a program that reads s and n from the user and then display the area of a
regular polygon constructed from these values.

"""

s = float(input("Insert the lenght of a side: "))
n = float(input("Insert the number of sides: "))


calc = (n*(s**2)) / (4*(math.tan(math.pi/n)))

print(calc)
