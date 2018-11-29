#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Introduction to Programming Exercises.

# Exercise 6: Tax and Tip.

"""
The program that you create for this exercise will begin by reading the cost
of a meal ordered at a restaurant from the user. Then you program will compute
the tax and tip for the meal. Use your local tax rate when computing the
amount of tax owing. Compute the tip as 18 percent of the meal amount
(without the tax). The output from your program should include the tax amount,
the tip amount, and the grand total for the meal including both the tip.
Format the output so that all of the values are displayed using two decimal
places.
"""

meal_cost = float(input("Insert the price of the meal:"))

TAX = 0.18
TIP = 0.10

total_tax = (meal_cost * TAX)
total_tip = (meal_cost * TIP)
grand_total = meal_cost + total_tax + total_tip

print("total tax", f'{total_tax:.2f}', "pesos")
print("total tip", f'{total_tip:.2f}', "pesos")
print("grand total", f'{grand_total:.2f}', "pesos")
