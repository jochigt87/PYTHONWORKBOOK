#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Loop Exercises.

# Exercise 80:Coin Flip Simulation.

"""
What's the minimum number of times you have to flip a coin before you canhave
three consecutive flips that result in the same outcome (either all three are
heads or all three are tails)? What's the maximum number of flips that might
be needed? How many flips are needed on average?. In this exercise we will
explore these questions by creating a program that simulates several series of
coin flips.
Create a program that uses Python's random number generator to simulate
flipping a coin several times. The simulated coin should be fair, meaning that
the probability of heads is equal to the probability of tails. Your program
should flip simulated coins until either 3 consecutive heads of 3 consecutive
tails occur. Display an H each time the outcome is heads, and a T each time
the outcome is tails, with all of the outcomes shown on the same line. Then
display the number of flips needed to reach 3 consecutive flips with outcome,
When your program is run it should perform the simulation 10 times and report
the average number of flips needed.
Sample output is shown below:

    H T T T (4 flips)
    H H T T H T H T T H H T H T T H T T T (19 flips)
    T T T (3 flips)
    T H H H (4 flips)
    H H H (3 flips)
    T H T T H T H H T T H H T H T H H H (18 flips)
    H T T H H H (6 flips)
    T H T T T (5 flips)
    T T H T T H T H T H H H (12 flips)
    T H T T T (5 flips)
    On average, 7.9 flips were needed.
"""
