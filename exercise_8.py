#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Introduction to Programming Exercises.

# Exercise 8:Widgets and Gizmos.

"""
An online retailer sells two products: widgets and gizmos. Each widget weighs
75 grams. Each gizmos weighs 112 grams. Write a program that reads the number
of widgets and the number of gizmos in a order from the user. Then your
program should compute and display the total weight of the order.
"""

WIDGET_WEIGHS = 75
GIZMOS_WEIGHS = 112

widgets = int(input("Insert the number of widgets do you want buy: "))
gizmos = int(input("Insert the number of widgets do you want buy: "))

total_weight = (WIDGET_WEIGHS * widgets + GIZMOS_WEIGHS * gizmos)
print(total_weight, "Grams")

