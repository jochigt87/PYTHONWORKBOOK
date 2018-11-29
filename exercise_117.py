#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Lists Exercises.

# Exercise 117:Line of Best Fit.

"""
A line of best fit is a straight line that best approximates a collection of n
data points. In this exercise, we will assume that each point in the
collection has an x coordinate and a y coordinate. The symbols x and y are
used to reprent the average x value in the collection and the average y value
in the collection respectively. The line of the best fit is reprented by the
equation y = mx + b where m and b are calculated using the following formulas:

        m  =  𝚺xy - (𝚺x)(𝚺y)
                    ---------
                        n
            ------------------
              𝚺x^2 - (𝚺x)^2
                    --------
                        n
            b = y - mx
    Write a program that reads a collection of points from the user. The user
will enter the x part of the first coordinate on its own line, followed by the
y part of the first coordinate on its own line. Allow the user to continue
entering coordinates, with the x and y parts each entered on their own line,
until your program reads a blank line for the x coordinate. Display the
formula for the line of the best fit in the form y = mx+b by replacing m and b
with the b with the values you calculated using the preceding formulas. For
example, if the user inputs the coordinates (1,1) (2, 2.1) and (3, 2.9) then
your program should display y = 0.95x + 0.1.
"""
