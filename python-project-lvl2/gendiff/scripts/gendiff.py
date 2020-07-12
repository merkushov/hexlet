#!/usr/bin/env python3

"""Gendiff script. Application start point"""

import gendiff.cli
import gendiff.engine


def main():
    args = gendiff.cli.parse_arguments(
        version=gendiff.engine.__version__
    )
    print(args)
    gendiff.engine.process(args.filepath_1, args.filepath_2)


if __name__ == "__main__":
    main()
