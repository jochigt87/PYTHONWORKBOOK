#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Introduction to Programming Exercises.

# Exercise : Area of a Room.

"""
Write a program that asks the user to enter the width and lenght of a room.
Once the values have been read, your program should compute and display the
area of the room. The lenght and the width will be entered as floating point
numbers. Include units in your prompt and output message; either feet or meter
depending on which unit you are more comfortable working with.
"""
width = float(input("Insert the width of room in meters: "))
lenght = float(input("Insert the lenght of room in meters: "))

total = width * lenght

print(total, "square meters")
