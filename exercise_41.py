#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# If Statement Exercises.

# Exercise 41:Note To Frequency.

"""
The following table lists an octave of music notes, begining with middle C,
along with their frequency.

-------------------------
Note    |Frequency (Hz) |
-------------------------
C4      |261.63
D4      |293.66
E4      |329.63
F4      |349.23
G4      |392.00
A4      |440.00
B4      |493.88

Begin by writing a program that reads the name of a note from the user and
display the note's frequency. Your program should support all of the notes
listed previously.

Once you have your program working correctly for the notes listed previously
you should add support for all of the notes from C0 to C8. While this could be
done by adding many additional cases to your if statement, such a solution in
cumbersome, inelegant relationship between notes in adjacent octaves. In
particular, the frequency of any note in octave n is half the frequency of the
corresponding note in octave n + 1. By using this relationship, you should be
able to add support for the additional notes without adding additional cases
to your if statement.

Hint: To complete this exercise you will need to extract individual characters
from the two-character note name so that you can work with the letter and the
octave number separately. Once you have separated the parts, computed the
frequency of the note in the fourth octave using the data in the table above.
Then divide the frequency by 2^4-x, where x is the octave number entered by
the user. This will halve or double the frequency the correct number of times.
"""


