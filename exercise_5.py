#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Introduction to Programming Exercises.

# Exercise 5: Bottle Deposits.

"""
In many jurisdictions a small deposit is added to drink containers to
to encourage people to recycle them. In one particular jurisdiction, drink
containers holding one liter or less have a $0.10 deposit, and drink
containers holding more than one one liter have a $0.25 deposit.

Write a program that reads the number of containers each size from the use.
Your program should continue by computing and displaying the refund that
will be received for returning those containers. Format the output so that it
includes a dollar sign and always display exactly two decimal places.
"""

LITER_LESS = 0.10
LITER_MORE = 0.25

less = int(input("Insert the drink containers one liter or less: "))
more = int(input("Insert the drink containers one liter or more: "))

refund = LITER_LESS * less + LITER_MORE * more

print(f'{refund:.2f}')
