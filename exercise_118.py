#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Lists Exercises.

# Exercise 118:.

"""
A standard deck of playing cards contains 52 cards. Each card has one of four
suits along with a value. The suits are normally spades, hearts, diamonds and
clubs while the values are 2 through 10, Jack, Queen, King and Ace.

Each playing card can be represent two characters. The first character is the
value of the card, with the values 2 through 9 being reprented directly. The
characters "T", "J", "Q", "K" and "A" are used to reprent the values 10, Jack,
Queen, King and Ace respectively. The second character is used to reprent the
suit of the card. It is normally a lowercase letter: "s" for spades, "h" for
hearts, "d" for diamonds and "c" for clubs. The following table provides
several examples of cards and their two-character representations.

------------------------------
Card            |Abbreviation|
------------------------------
Jack of Spades  |Js          |
Two of clubs    |2c          |
Ten of diamonds |Td          |
Ace of hearts   |Ah          |
Nine of spades  |9s          |
------------------------------

Begin by writing a function named createDeck. It will use loops to create a
complete deck of cards by storing the two-character abbreviations for all 52
cards into a list. Return the list of cards as the function's only result.
Your function will not take any parameters.

Write a second function named shuffle that randomizes the order of the cards
in a lost. One technique that can be used to shuffle the cards is to visit
each element in the list and swap it with another random element in the list.
You must write your own loop for shuffling the cards. You cannot make use of
Python's built-in shuffle function.

Use both of the functions described in the previous paragraphs to create a
main program that displays a deck of cards before and after it has been
shuffled. Ensure that your main program only runs when your functions have not
been imported into another file.

"""
