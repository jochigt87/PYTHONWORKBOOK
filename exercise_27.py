#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Introduction to Programming Exercises.

# Exercise 27:Body Mass Index.

"""
Write a program that computes the body mass index (BMI) of an individual. Your
program should begin by reading a height and weight from the user. Then it
should use one of the following two formulas to compute the BMI before
displaying it. If you read the height in inches and the weight in pounds then
body mass index is computed using the following formula:


                    BMI = weight
                        ----------  x 703
                        height * height

If you read the height in meters and the weight in kilograms then body mass
index is computed using this slightly simpler formula:


                    BMI =      weight
                        --------------------
                           height * height


"""
height_inches = float(input("Insert you height in inches: "))
weight_pounds = float(input("Insert you weight in pounds:" ))

body_max = ((weight_pounds) / (height_inches**2)) * 703

print(body_max)
