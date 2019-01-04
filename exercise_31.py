#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Introduction to Programming Exercises.

# Exercise 31:Sum of the Digits in an Integer.

"""
Develop a program that reads a four-digit integer from the user and displays
the sum of the digits in the number. For example, if the user enters 3141 then
your program should display 3 + 1 + 4 + 1 = 9.
"""

sumatoria = int(input("Insert 4 Digits:"))

# Extract the last digit

a = sumatoria%10

# Extract the third digit

b = sumatoria%100//10

# Extract the second digit

c = sumatoria%1000//100

# Extract the first digit

d = sumatoria%10000//1000

# Show the result on screen.

print(a + b + c + d)
