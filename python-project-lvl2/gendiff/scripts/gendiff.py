#!/usr/bin/env python3

"""Gendiff script. Application start point"""

import gendiff.cli
import gendiff.core


def main():
    """
        The main function of launching an application in the console.
    """
    try:

        # process command line arguments
        args = gendiff.cli.parse_arguments(
            version=gendiff.core.__version__
        )

        # get difference between two files
        diff_data = gendiff.core.diff_between_files(
            args["filepath_1"],
            args["filepath_2"]
        )

        # format the received data into human readable format
        diff_text = gendiff.core.format(diff_data, args["format"])

        # output difference to the console
        gendiff.cli.output(diff_text)

    except Exception as error:
        gendiff.cli.output("An error occurred: {}".format(error))


if __name__ == "__main__":
    main()
