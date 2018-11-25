#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Introduction to Programming Exercises.

# Exercise 12: Distance Between Two Points on Earth.

"""
The surface of the Earth is curved, and the distance between degrees of
longitude varies with latitude. As a result, finding the distance between
two points on the surface of the Earth is more complicated than simply using
the Pythagorean Teorem. Let (t₁,g₂) and (t₁,g₂) be the latitude and longitude
of two points on the Earth's surface. The distance between these points,
following the surface of the Earth, in kilometers is:

    distance = 6371.01 * arccos(sin(t₁) * sin(t₂) + cos(t₁) * cos(t₂) * cos(g₁ - g₂))

    👉Hint: The value 6371.01 in the previous equation wasn't selected at
            random. It is the average radius of the Earth in kilometers.

Create a program that allows the user to enter the latitude and the longitude
of two points on the Earth in degrees. Your program should display the
distance between the points, following the surface of the earth, in kilometers

    👉Hint: Python's trigonometric functions operate in radians. As result,
            you will need to convert the user's input from degrees to radians
            before computing the distance with the formula discussed
            previously. The math module contains a function named radians
            which converts from degrees to radians.
"""


