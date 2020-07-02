#!/usr/bin/env python3

import brain_games.engine
from brain_games.games import even


def main():
    brain_games.engine.run(even)


if __name__ == "__main__":
    main()
