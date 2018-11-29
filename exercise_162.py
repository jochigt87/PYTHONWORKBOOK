#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File and Exceptions Exercises.

# Exercise 162: Consistent Line Lenghts.

"""
While 80 characters is common width for a terminal windows, some terminals are
narrow or wider. This can present challenges when displaying documents
containing paragraphs of text. The lines might be too long and wrap, making
them difficult to read, or they might be too short and fail to make use of the
available space.
    Write a program that opens a file and displays it so that each line is
filled as full as possible. If you read a line that is too long then your
program should break it up into words and add words to the current line until
it is full. Then your program should start a new line and display the
remaining words. Similarly, if you read a line that is too short then you will
need to use words from the next line of the file to finish filling the current
line of output. For example, consider a file containing the following lines
from "Alice's Adventures in Wonderland":
    Alice was
    Beginning to get very tired of sitting by her
    sister
    on the bank, and of having nothing to do: once
    or twice she had peeped into the book her sister
    was reading, but it had
    no
    pictures or conversations in it,  "and what is
    the use of a book, " thought Alice, "without
    pictures or conversations?"

When formatted for a line lenght of 50 characters, it should be displayed as:

    Alice was Beginning to get very tired of sitting
    by her sister on the bank, and of having nothing
    to do: once or twice she had peeped into the book
    her sister was reading, but it had no pictures or
    conversations in it,  "and what is the use of a
    book, " thought Alice, "without pictures or
    conversations?"

Ensure that your program works correctly for files containing multiple
paragraphs of text. You can detect the end of one paragraph and the beggining
of the next by looking for lines that are empty once the end of line marker
has been removed. You may perform error checking if you want to, but it is not
required for this exercise.

Hint: Use a constant to represent the maximum line lenght. This will make it
easier to update the program when the windows size changes.

"""
