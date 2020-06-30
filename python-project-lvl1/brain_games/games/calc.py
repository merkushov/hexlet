#!/usr/bin/env python3

"""The module that generates the game according to the given rules"""

from random import randint

TASK = 'What is the result of the expression?'


def get_round():
    number1 = randint(0, 100)
    number2 = randint(0, 100)
    math = randint(0, 2)

    if math == 0:
        return (
            "{0} + {1}".format(number1, number2),
            str(number1 + number2)
        )
    elif math == 1:
        return (
            "{0} - {1}".format(number1, number2),
            str(number1 - number2)
        )
    else:
        return(
            "{0} * {1}".format(number1, number2),
            str(number1 * number2)
        )
