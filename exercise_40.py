#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# If Statement Exercises.

# Exercise 40:Name that Triangle.

"""
A triangle can be classified base on the lenghts of its sides as equilateral,
isosceles or scalene. All 3 sides of an equilateral triangle have the same
lenght, and a third side that is a different lenght. If all of the sides have
different lenghts then the triangle is scalene.
Write a program that reads the lenghts of 3 sides of a triangle from the user.
Display a message indicating the type of the triangle.
"""

a = int(input("Insert the lenght: "))
b = int(input("Insert the lenght: "))
c = int(input("Insert the lenght: "))

if a == b and c == a:
    print("Equilateral")
elif (a==b) or (a==c) or (b==c):
    print("Isoceles")
elif a != b and c != a:
    print("Scalene")
