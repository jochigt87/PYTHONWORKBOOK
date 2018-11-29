#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Introduction to Programming Exercises.

# Exercise 18: Volume of a Cylinder.

"""
The volume of a cylinder can be computed by multiplying the area of its
circular base by its height. Write a program that reads the radius of the
cylinder, along with its height, from the user and computes its volume.
Display the result rounded to one decimal place.
"""
import math
radius = float(input("Insert the radius of cylinder: "))
height = float(input("Insert the height of cylinder: "))

pi = math.pi

volume = ((radius**2) * height) * (pi)
print("the volume of cylinder is:", f'{volume:.1f}')

