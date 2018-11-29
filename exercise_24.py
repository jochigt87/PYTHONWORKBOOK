#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Introduction to Programming Exercises.

# Exercise 24: Units of Time.

"""
Create a program that reads a duration from the user as a number of days,
hours, minutes, and seconds. Compute and display the total number of seconds
represented by this duration.
"""

ONE_DAY = 86400
ONE_HOUR = 3600
ONE_MIN = 60

days = float(input("Insert the days: "))
hours = float(input("Insert the hours: "))
minutes = float(input("Insert the minutes: "))

total = (days * ONE_DAY) + (hours + ONE_HOUR) + (minutes * ONE_MIN)
print(total, "seconds")
