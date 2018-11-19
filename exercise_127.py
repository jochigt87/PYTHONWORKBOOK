#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Lists Exercises.

# Exercise 127:The Sieve of Erastosthenes.

"""
The Sieve of Erastosthenes is a technique that was developed more thatn 2,000
years ago to easily find all the prime numbers between 2 and some limit, say
100. A description of the algorithm follows:

    Write down all of the numbers from 0 to the limit
    Cross out 0 and 1 because they are not prime

    Set p equal to 2
    While p is less than the limit do
        Cross out all multiples of p (but not p itself)
        Set p equal to the next number in the list that is not crossed out


    Report all of the numbers that have not been crossed out as prime

    The key to this algorithm is that it is relatively easy to cross out every
n number on a piece of paper. This is also an easy task for a computer---a for
loop can simulate this behavior when a third parameter is provided to the
range function. When a number is crossed out, we know that it is no longer
prime, but it still occupies space on the piece of paper, and must still be
considered when computing later prime numbers. As a result, you should not
simulate crossing out a number by removing it from the list. Instead, you
should simulate crossing out a number by replacing it with 0. Then, once the
algorithm completes, all of the non-zero values in the list are prime.

Create a Python program that uses this algorithm to display all of the prime
numbers between 2 and a limit entered by the user. if you implement the
algorithm correctly you should be able to display all of the prime numbers
less than 1,000,000 in few seconds.

This algorithm for finding prime numbers is not Erastosthenes' only claim to
fame. his other noteworthy accomplishments include calculating the
circumference of the Earth and the tilt of the Earth's axis. He also served as
the Chief Librarian at the Library of Alexandria.
"""
