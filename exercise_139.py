#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Dictionary Exercises.

# Exercise 139:Checking for a Winning Card.

"""
A winning Bingo card contains a line of 5 numbers that have all been called.
Players normally mark the numbers that have been called by crossing them out
or marking them with a Bingo dauber. In our implementation we will mark that a
number has been called by replacing it with a 0 in the Bingo card dictionary.
    Write a function that takes a dictionary representing a Bingo card as its
only parameter. If the card contains a line of five zeros (vertical,
horizontal or diagonal) then your function should return True, indicating that
the card has won. Otherwise the function should return False.
    Create a main program that demonstrates your function by creating several
Bingo cards, displaying them, and indicating whether or not they contain a
winning line. You should demonstrate your function with at least one card with
horizontal line, at least one card with vertical line, at least one card with
diagonal line, and at least one card with crossed out but does not contain a
winning line. You will probably want to import your solution to Exercise 138
when completing this exercise.

Hint: Because there are no negative numbers on a Bingo card, finding a line of
5 zeros is the same problem as finding a line of 5 entries that sum to zero.
You may find the summation problem easier to solve.
"""
