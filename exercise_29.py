#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Introduction to Programming Exercises.

# Exercise 29: Celsius to Fahrenheit and Kelvin.

"""
Write a program that begins by reading a temperature from the user in degrees
Celsius. Then your program should display the equivalent temperature in
degrees Fahrenheit and degrees Kelvin. The calculations needed to convert
between different units of temperature can be found on the internet.
"""

celsius = float(input("Insert the temperature in celsius degrees: "))

fahrenheit = (celsius *1.8000) + 32
kelvin = (celsius + 273.15)

print(celsius, "Celsius Degrees are: ")
print(fahrenheit, "Fahrenheit Degrees")
print(kelvin, "Kelvin Degrees")
