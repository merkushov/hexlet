#!/usr/bin/env python3

"""Gendiff script. Application start point"""

import gendiff.cli
import gendiff.core


def main():
    # process command line arguments
    args = gendiff.cli.parse_arguments(
        version=gendiff.core.__version__
    )

    # get difference between two files
    diff_data = gendiff.core.diff_between_files(
        args["filepath_1"],
        args["filepath_2"]
    )

    # output difference to the console
    diff_text = gendiff.core.format(diff_data, args["format"])
    gendiff.cli.output(diff_text)


if __name__ == "__main__":
    main()
