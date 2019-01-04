#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Introduction to Programming Exercises.

# Exercise 32: Sort 3 Integers.

"""
Create a program that reads three integers from the user and displays them in
sorted order (from smallest to largest). Use the min and max functions to find
the smallest and largest values. The middle value can be found by computing
the sum of all three values, and then subtracting the minimum value the
maximum value.
"""
import sys 
sys.
digit = int(input("Insert three digits: "))

a = digit//100

b = digit//10%10

c = digit%10

smaller = min(a, b, c)
largest = max(a, b, c)

middle = (a+b+c-smaller-largest)

print("smaller", smaller, "largest", largest, "middle ", middle)
