#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Introduction to Programming Exercises.

# Exercise 16: Area and Volume.

"""
Write a program that begins by reading a radius, r, from the user. The program
will continue by computing and displaying the area of a circle with radius r
and the volume of a sphere with radius r. Use the pi constant in the math
module in your calculations.

    👉 Hint: The area of a circle is computed using the formula area = pi*r^2,
    The volume of sphere is computed using the formula volume 4/3*pi*r^3.
"""
import math

pi = math.pi
radius = float(input("Insert the radius: " ))

area = pi * (radius**2)
volume = (4/3) * pi * (radius**3)

print("The Area of circle is: ", f'{area:.2f}')
print("The Volume of sphere is: ", f'{volume:.2f}')
