#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# If Statement Exercises.

# Exercise 34:.

"""
Write a program that reads an integer from the user. Then your program should
display a message indicating whether the integer is even or odd.
"""

number = int(input("Insert a number: "))

if number % 2 == 0:
    print(number, "is even")
elif number % 2 == 1:
    print(number, "is odd")
