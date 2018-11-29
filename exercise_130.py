#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Dictionary Exercises.

# Exercise 130:Text Messaging.

"""
On some basic cell phones, text messages can be sent using the numeric keypad.
Because each key has multiple letters associated with it, multiple key presses
are needed for most letters. Pressing the number once generates the first
letter on the key. Pressing the number 2, 3, 4, or 5 times generates the
second, third, fourth of fifth character listed for that key.

Key         | Symbols
--------------------------
1           |.,?!:
2           |A B C
3           |D E F
4           |G H I
5           |J K L
6           |M N O
7           |P Q R S
8           |T U V
9           |W X Y Z
0           |space
--------------------------

Write a program that display the keys presses that must be made to enter a
text message read from the user. Construct a dictionary that maps from each
letter or symbol to the key presses. Then use the dictionary to generate and
display the presses for the user's message. For example, if the user enters
Hello, World! then your program should output 4433555555666110966677755531111.
Ensure that program handles bith uppercase and lowercase letters. Ignore any
characters that aren't listed in the table above such as semicolons and
brackets.

"""
