#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File and Exceptions Exercises.

# Exercise 160: Redacting Text in a File.

"""
Sensitive information is often removed, or redacted, from documents before
they are released to the public. When the documents are released it is common
for the redacted text to be replaced with black bars.
    In this exercise you will write a program that redacts all occurrences of
sensitive words in a text file by replacing them with asterisks. Your program
should redact sensitive words wherever they occur, even if they occur in the
middle of another word. The list of sensitive words will be provided in a
separate text file. Save the redacted version of the original text in a new
file. The names of the original text file, sensitive words file, and redacted
file will all be provided by the user.

Hint: You may find the replace method for string helpful when completing this
exercise. Information about the replace method can either be found in your
textbook or on the internet.

For an added challenge, extend you program so that it redacts words in case
insensitive manner. For example, if exam appears in the list of sensitive
words then redact exam, Exam, ExaM and EXAM, among other possible
capitalizations.
"""
