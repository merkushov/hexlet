"""The module that generates the game according to the given rules"""

from random import randint

TASK = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 7


def get_round():
    """
        The function of generating one round of the game.
        Returns a tuple consisting of 2 elements:
            - the value for the round of the game
            - the correct answer in this round
    """
    progression = []
    start = randint(1, 50)
    step = randint(1, 10)
    stop = start + step * PROGRESSION_LENGTH

    for i in range(start, stop, step):
        progression.append(str(i))

    remove_index = randint(0, PROGRESSION_LENGTH - 1)
    true_answer = progression[remove_index]
    progression[remove_index] = '..'

    return (' '.join(progression), true_answer)
