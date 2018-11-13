#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Loop Exercises.

# Exercise 70:Caesar Cipher.

"""
One of the first known example of encryption was used by Julius Caesar. Caesar
needed to provide written instructions to his generals, but he didn't want his
enemies to learn his plans if the message slipped into their hands. As result,
he developed what later became known as the Caesar Cipher.

The idea behind this cipher is simple (and as result, it provides no
protection againt modern code breaking techniques). Each letter in the
original message is shifted by 3 places. As result, A becomes D, B becomes E,
C becomes D, etc. The last three letters in the alphabet are wrapped around to
the beginnings: X becomes A, Y becomes B and Z becomes C. Non-letter
characters are not modified by the cipher.

Write a program thhat implements a Caesar Cipher. Allow the user to supply the
message and the shift amount, and then display the shifted message. Ensure
that your program encodes both uppercase and lowercase letters. Your program
should also support negative shift values so that it can be used both to
encode messages and decode messages.
"""
