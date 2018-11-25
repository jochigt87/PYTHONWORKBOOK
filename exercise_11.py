#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Introduction to Programming Exercises.

# Exercise 11: Fuel Efficiency.

"""
In the United States, fuel efficiency for vehicules is normally expressed in
miles-per-gallon(MPG). In Canada, fuel efficiency is normally expressed in
litters-per-hundred kilometers(L/100km). Use your research skills to determine
how to convert from MPG to L/100km
"""

mpg = float(input("Insert Miles-per-gallon: "))

LITER_100_KM = (100 * 3.785411784) / (1.609344 * mpg)
total = LITER_100_KM
print(f'{total:.2f}', "L/100km")
