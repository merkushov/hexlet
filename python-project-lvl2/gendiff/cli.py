'''The module works with the command line interface'''

import argparse


def parse_arguments(version=None):
    '''
        Command line argument parsing method.

        Returns the dictionary from the resulting values.
    '''
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Generate difference between two files',
        allow_abbrev=False
    )
    parser.add_argument(
        '-f',
        '--format',
        choices=['dictionary', 'json', 'plain'],
        default='dictionary',
        help='Set output format. Default %(default)s',
        type=str
    )
    parser.add_argument(
        'file1',
        help='''
            File number 1 for comparison.
            Must be in .json or .yaml format.
        ''',
        type=argparse.FileType(mode='r', encoding='UTF-8'),
    )
    parser.add_argument(
        'file2',
        help='''
            File number 2 for comparison.
            Must be in .json or .yaml format.
        ''',
        type=argparse.FileType(mode='r', encoding='UTF-8'),
    )
    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s {}'.format(version)
    )

    args = parser.parse_args()

    return {
        "filepath_1": args.file1.name,
        "filepath_2": args.file2.name,
        "format": args.format
    }


def output(string):
    print(string, end='')
