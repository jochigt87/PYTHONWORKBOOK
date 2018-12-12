#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Introduction to Programming Exercises.

# Exercise 26: Current Time.
import datetime
import time
"""
Python includes a library of functions for working with time, including a
function called asctime in the time module. It reads the current time from the
computer's internal clock and returns it in a human-readable format. Write a
program that display the current time and date. Your program will not require
any input from the user.
"""

today = time.asctime()

print(today)
