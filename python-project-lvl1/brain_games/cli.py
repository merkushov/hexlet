"""Module for processing data from the command line"""

import prompt


def welcome_user(name):
    """Show welcome message in the command line"""
    print('Hello, {}!'.format(name))


def show_task_discription(task):
    """Displays a message with a description of the game in the console"""
    print('Welcome to the Brain Games!\nYour task is {}'.format(task))


def show_question(question):
    """Displays a game question"""
    print('Question: {}'.format(question))


def show_success(name):
    """Displays a message in the console, in case of a successful answer"""
    print('Correct!\n')


def show_fail(name, answer, true_answer):
    """Displays a message in the console if the answer is incorrect"""
    print(
        'Your answer is wrong. Correct answer was {0}\nLet\'s try angain, {1}'
        .format(true_answer, name)
    )


def show_win(name):
    """Displays the final message, in case of victory in the game"""
    print('Congratulations, {}! You win.'.format(name))


def get_user_name():
    """Request player name"""
    name = prompt.string('May I have your name? ')
    return name


def get_user_answer():
    """Accept the answer to the question from the player"""
    answer = prompt.string('You answer: ')
    return answer
