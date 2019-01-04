#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Introduction to Programming Exercises.

# Exercise 33: Day Old Bread.

"""
A bakery sells loaves of bread for $3.49 each. Day old bread is discounted by
60 percent. Write a program that begins by reading the number of loaves of day
old bread beings purchased from the user. Then your program should display the
regular price for the bread, the discount because it is a day old, and the
total price. All of the values should be displayed using two decimal places,
and the decimal points in all of the numbers should be aligned when reasonable
values are entered by the user.
"""

loaves_purchased = int(input("Inser the number of loaves you want buy: "))

discount = 0.60

price_loaves = 3.49

discounted_price = (discount * loaves_purchased)

regular_price = (price_loaves * loaves_purchased)

price_with_discount = (regular_price - discounted_price)

print("Regular Price: ", f'{regular_price:.2f}')

print("Price with Discount:", f'{price_with_discount:.2f}')

print("Discount:", f'{discounted_price:.2f}')
