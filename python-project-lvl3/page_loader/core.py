__version__ = '0.1.1'

import logging
import sys
import page_loader.cli
import page_loader.config as config
import page_loader.fetcher
import page_loader.keeper


def _convert_url_to_filename(url: str) -> str:
    '''
        Function converts url to human readable filename
    '''

    # the stub
    return 'index.html'


def download(url: str, output_dir: str = config.default_output_dir) -> bool:
    '''
        The function downloads the source data
        and saves it to a local directory
    '''
    logger = logging.getLogger()
    success = False

    try:
        logger.debug('Receiving data by address: {}'.format(url))
        content = page_loader.fetcher.fetch_data_by_url(url)

        filename = _convert_url_to_filename(url)

        logger.debug(
            "Saving the received data into a file '{}' of the '{}' directory:"
            .format(filename, output_dir)
        )
        success = page_loader.keeper.save_source_locally(
            filename, output_dir, content)
    except Exception:
        success = False

    return success


def main():
    '''
        The main function of launching the Application
        in the console.
    '''
    args = page_loader.cli.parse_arguments(__version__)

    log_level = args['log_level']
    logging.basicConfig(filename='loader.log', level=log_level.upper())
    logger = logging.getLogger()

    logger.debug(
        '''
            Application launch options:
                url: {}
                output: {}
                log_level: {}
        '''.format(args['url'], args['output'], args['log_level'])
    )

    success = download(args['url'], args['output'])
    if success is True:
        logger.info('Url {} successfully saved'.format(args['url']))
        sys.exit(0)
    else:
        logger.error("Can't save Url {}".format(args['url']))
        sys.exit(1)
