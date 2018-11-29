#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Introduction to Programming Exercises.

# Exercise 21:Area of a Triangle.

"""
The area of a triangle can be computed using the following formula, where b its
the lenght of the base of the triangle, and h is its height:

area = b*h/2

Write a program that allows the user to enter values for b and h. The program
should then compute and display the area of a triangle with base lenght b and
height h.
"""

b = float(input("Insert the base of Triangle in meters: "))
h = float(input("Insert the height of Triangle in meters: "))

area = (b*h)/2
print("The area of Triangle is: ", f'{area:.2f}', "meters")
