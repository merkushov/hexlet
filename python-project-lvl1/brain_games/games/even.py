#!/usr/bin/env python3

"""The module that generates the game according to the given rules"""

from random import randint

TASK = 'Answer "yes" if number even therwise answer "no"'


def get_round():
    """
        The function of generating one round of the game.
        Returns a tuple consisting of 2 elements:
            - the value for the round of the game
            - the correct answer in this round
    """
    number = randint(1, 100)

    if number % 2 == 0:
        return (number, 'yes')
    else:
        return (number, 'no')
