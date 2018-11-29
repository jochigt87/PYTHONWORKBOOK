#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Introduction to Programming Exercises.

# Exercise 25:Units of Time(Again).

"""
In this exercise you will reverse the process described in the previous
exercise. Develop a program that begins by reading a number of seconds from
the user. Then your program should display the equivalent amount of time in the
form D:HH:MM:SS, where D,HH, MM, SS represent days, hours, minutes and seconds
respectively. The hours, minutes, and seconds should all be formatted so that
they occupy exactly two digits, with a leading 0 displayed if neccesary.
"""

ONE_DAY =0.00001157407
ONE_HOUR = 0.0002777778
ONE_MIN = 0.016666668
ONE_SECOND = 1

seconds = float(input("Insert the amount of seconds: "))

days = (seconds * ONE_DAY)
hours = (seconds * ONE_HOUR)
minutes = (seconds * ONE_MIN)

print("D",f'{days:.2f}', "HH",f'{hours:.2f}', "MM",f'{minutes:.2f}', seconds)
