#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Introduction to Programming Exercises.

# Exercise 10: Arithmetic.

import math
"""
Create a program that reads two integers, a and b, from the user. Your program
should compute and display:

    👉 The sum of a and b.
    👉 The difference when b is subtracted from a.
    👉 The product of a and b.
    👉 The quotient when a is divided by b.
    👉 The result of log Base 10 ^a.

    Hint: You will probably find the log10 function in the math module helpful
    for computing the second last item in the list.
ok
"""

a = int(input("Insert a: "))
b = int(input("Insert b: "))

print("a + b :", a + b)
print("a - b :", a-b)
print("a * b:", a*b)
print(" a // b:", a//b)
print("log base 10 of a is :", math.log10(a))
