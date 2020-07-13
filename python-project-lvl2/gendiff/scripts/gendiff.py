#!/usr/bin/env python3

"""Gendiff script. Application start point"""

import gendiff.cli
import gendiff.engine


def main():
    # process command line arguments
    args = gendiff.cli.parse_arguments(
        version=gendiff.engine.__version__
    )

    # get difference between two files
    diff_data = gendiff.engine.diff_between_files(
        args["filepath_1"],
        args["filepath_2"]
    )

    # output difference to the console
    diff_text = gendiff.engine.format(diff_data, args["format"])
    gendiff.cli.output(diff_text)


if __name__ == "__main__":
    main()
