#!/usr/bin/env python3

"""Gendiff script. Application start point"""

import gendiff.cli
import gendiff.engine


def main():
    print("Hello! I'm gendiff")
    args = gendiff.cli.parse_arguments(
        version=gendiff.engine.__version__
    )
    print(args)


if __name__ == "__main__":
    main()
