#!/usr/bin/env python3

"""The module that defines the steps of the game"""

import brain_games.cli

ROUNDS = 3


def run(game):
    """The main function of launching the game"""

    name = brain_games.cli.get_user_name()
    brain_games.cli.welcome_user(name)
    brain_games.cli.show_task_discription(game.TASK)

    for _ in range(ROUNDS):
        question, true_answer = game.get_round()
        brain_games.cli.show_question(question)
        answer = brain_games.cli.get_user_answer()

        if answer != true_answer:
            brain_games.cli.show_fail(name, answer, true_answer)
            return

        brain_games.cli.show_success(name)

    brain_games.cli.show_win(name)

    return 1
