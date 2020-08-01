__version__ = '0.1.0'

import page_loader.cli


def main():
    """
        The main function of launching the Application
        in the console.
    """
    args = page_loader.cli.parse_arguments(__version__)
    print("Load page: {}".format(args['url']))
