"""The module that generates the game according to the given rules"""

from random import randint

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    """
        The function to check if a number is prime.
        Returns True if the number is prime and False otherwise.
    """
    if (n <= 1):
        return False

    if (n % 2 == 0):
        return False

    for i in range(3, n, 2):
        if (n % i == 0):
            return False

    return True


def get_round():
    """
        The function of generating one round of the game.
        Returns a tuple consisting of 2 elements:
            - the value for the round of the game
            - the correct answer in this round
    """
    number = randint(1, 1000)

    if is_prime(number):
        return (str(number), 'yes')
    else:
        return (str(number), 'no')
