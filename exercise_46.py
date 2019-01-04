#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# If Statement Exercises.

# Exercise 46: Season from Month and Day.

"""
The year is divide into four seasons: spring, summer, fall and winter. While
the exact dates that the seasons change vary a little bit from year to year
because of the way that the calendar is constructed, we will use the following
dates for this exercise:

-----------------------------
Season      |First Day
-----------------------------
Spring      |March 20
Summer      |June 21
Fall        |September 22
Winter      |December 21

Create a program that reads a month and day from the user. The user will enter
the name of the month as a string, followed by the day within the month as an
integer. Then your program should display the season associated with the date
that was entered.
"""
season = input("Insert a month:")
day = input("Insert a day: ")


if season == "March" or season == "Abril" or season == "May":
    if day == "20":
        print("Spring")

elif season == "June" or season == "July" or season == "August":
    if day == "21":
        print("Summer")

elif season == "September" or season == "October" or season == "November":
    if day == "22":
        print("Winter")
