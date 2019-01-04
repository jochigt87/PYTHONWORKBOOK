#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# If Statement Exercises.

# Exercise 44:Date to Holiday Name.

"""
Canada has three national holidays which fall on the same dates each year.

-------------------------
Holiday         |Date
New year's day  |January 1
Canada day      |July 1
Christmas day   |December 25

Write a program that reads a month and day from the user. If the month and the
day match one of the holidays listed previously then your program should
display the holiday's name. Otherwise your program should indicate that the
entered month and day do not correspond to a fixed-date holiday.

Hint:
Canada has two additional national holidays, Good Friday and Labour Day, whose
dates vary from year to year. There are numerous provincial and territorial
holidays, some of which have fixed dates, and some of which have variable
dates. We will not consider any of these additional holidays in this exercise.
"""

day = input("Insert the day: ")
month = input("Insert the month: ")

if month == "january" or month == "January":
    if day == "1":
        print("New year's day")
elif month == "July" or month == "july":
    if day == "1":
        print("Canada Day")
elif month == "December" or month == "december":
    if day == "25":
        print("Christmas Day")
else:
    print("The date inserted not correspond with the stored")
