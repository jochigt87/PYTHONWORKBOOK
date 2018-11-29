#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Lists Exercises.

# Exercise 123: Infix to Postfix.

"""
Mathematical expressions are often written in infix form, where operators
appear between the operands on which they act. While this is a common form, it
is also possible to express mathematical expressions in postfix form, where
the operator appears after both operands. For example, the infix expression 3
+ 4 is written as 3 4 + in postfix form. One can convert an infix expression
to postfix form using the following algorithm:

    Create a new empty list, operators
    Create a new empty list, postfix

    For each token in the infix expression
        If the token is an integer then
            Add the token to the end of postfix
        If the token is an operator then
            While operators is not empty and
                the last item in operators is not an open parenthesis and
                precedence(token) < precedence(last item in operators) do
             Remove the last item from operators and add it to postfix
            Add toke to the end of operators
        If the token is an open parenthesis then
            Add token to the end of operators
        If the token is a close parenthesis then
            While the last item in operators is not an open parenthesis do
                Remove the last item from operators and add it to postfix
            Remove the open parenthesis from operators

    While operators is not the empty list do
        Remove the last item from operators and add it to postfix

    Return postfix as the result of the algorithm

    Use your solution to Exercise 122 to tokenize a mathematical expression.
Then use the algorithm above to transform the expression from infix form to
postfix form. Your code that implements the precceding algorithm should reside
in a function that takes a list of tokens representing an infix expression as
its only parameter. It should return a list of tokens representing the
equivalent postfix expression as its only result. Include a main program that
demonstrates your infix to postfix function by reading an expression from the
user in infix form and displaying it in postfix form.

The porpuse of converting from infix form to postfix form will become apparent
when you read Exercise 124. You may find your solutions to Exercises 90 and 91
helpful when completiong this problem.

The algorithm provided in Exercises 123 and 124 do not perform any error
checking. As a result, you may crash your program or receive incorrect results
if you provide them with invalid input. These algorithm can be extended to
detect invalid input and respond to it in a reasonable manner. Doing so is
left as an indepent study exercise for the interested student.
"""
