'''The module works with the command line interface'''

import argparse


def parse_arguments(version=None):
    '''
        Command line argument parsing method.
        Return a dictionary containing the arguments
        read from the command line.
    '''
    parser = argparse.ArgumentParser(
        prog='page_loader',
        description='''
            Downloads a web page with all dependencies
            to a local directory
        ''',
        allow_abbrev=False
    )
    parser.add_argument(
        '-o',
        '--output',
        default='./page_loader_data',
        help='Set local directory for web page. Default %(default)s',
        type=str
    )
    parser.add_argument(
        '-l',
        '--log_level',
        choices=['error', 'info', 'debug'],
        default='debug',
        help='Set log level. Default %(default)s',
        type=str
    )
    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s {}'.format(version)
    )
    parser.add_argument(
        'url',
        help='Specify the address of the page to be downloaded',
        type=str
    )

    args = parser.parse_args()

    return {
        "url": args.url,
        "output": args.output,
        "log_level": args.log_level,
    }
