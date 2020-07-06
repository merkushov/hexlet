"""The module that generates the game according to the given rules"""

from random import randint

TASK = 'Find the greatest common divisor of given numbers.'


def get_round():
    """
        The function of generating one round of the game.
        Returns a tuple consisting of 2 elements:
            - the value for the round of the game
            - the correct answer in this round
    """
    number1 = randint(1, 50)
    number2 = randint(1, 50)

    question = '{0} {1}'.format(number1, number2)

    # Euclidean algorithm for Greatest common division
    while number2 != 0:
        number1, number2 = number2, number1 % number2

    return (question, str(number1))
