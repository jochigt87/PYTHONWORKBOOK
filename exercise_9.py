#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Introduction to Programming Exercises.

# Exercise 9:Compound Interest.

"""
Pretend that you have just opened a new savings account that earns 4 percent
interest per year. The interest that you earn is paid at the end of the year,
and is added to the balance of the saving account. Write a program that begins
by reading the amount of money deposited into the account from the user. Then
your program should compute and display the amount in the savings account
after 1, 2, and 3 years. Display each amount so that it is rounded to 2
decimal places.
"""

INTEREST_PER_YEAR = 0.04

deposited = float(input("Insert the amount do you want deposit: "))

first_year = (deposited * INTEREST_PER_YEAR) + deposited
second_year = (first_year * INTEREST_PER_YEAR) + first_year
third_year = (second_year * INTEREST_PER_YEAR) + second_year

print("First Year", f'{first_year:.2f}')
print("Second Year", f'{second_year:.2f}')
print("Third Year",f'{third_year:.2f}')
