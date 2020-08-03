'''
    This module contains everything related to receivint data
    from a remote source. The remote source is a web-page or image
    or javascript/css file
'''

import logging
import requests

logger = logging.getLogger()


def fetch_data_by_url(url: str) -> str:
    '''
        The function downloads the requested resource by its URL
        from the Internet

        Args:
            url: str
                Uniform Resource Identifier on the Internet

        Returns:
            resource_content: str
                Content of the downloaded resource in string format

        Raises:
            ConnectionError
    '''
    content_text = ''
    try:
        r = requests.get(url)

        # throws an exception if the HTTP status code
        # is greater than or equal to 400
        r.raise_for_status()

        content_text = r.text
    except requests.exceptions.RequestException as error:
        # Catch any exception in 'requests'
        # RequestException is a base exception for everthing else
        logger.error('fetcher got an error: {}'.format(error))
        raise ConnectionError

    return content_text
