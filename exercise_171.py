#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Recursion Exercises.

# Exercise 171:Spelling with Element Symbols.

"""
Each chemical element has a standard symbol that is one, two or three letters
long. One game that some people like to play is to determine whether or not a
word can be spelled using only element symbols. For example, silicon can be
spelled using the symbols Si, Li, C, O and N. However, hydrogen can not be
spelled with any combination of element symbols.
Write a recursive function that determines whether or not a word can be
spelled using only element symbols. Your function will take two parameters:
the word that you are trying to spell and a list of the symbols that can used.
Your function will return two results: a Boolean value indicating whether or
not a spelling was found, and the string of symbols used to achieve the
spelling (or an empty string if no spelling exists). Your function should
ignore capitalization when searching for a spelling.
    Create a program that uses your function to find and display all of the
element names that can be spelled using only element symbols. Display the
names of the elemets along with the sequences of symbols. For example, one
line of your output will be:

    Silver can be spelled as SiLvEr

    Your program will use the elements data set, which can be downloaded from
the author's website. This data set includes the names and symbols of all 118
chemical elements.
"""
