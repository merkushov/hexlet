"""The main module containing the core logic of the application"""

__version__ = "0.1.2"

from bs4 import BeautifulSoup
import logging
import sys
import page_loader.cli
import page_loader.config as config
import page_loader.fetcher
import page_loader.keeper


def _convert_url_to_filename(url: str) -> str:
    """
    Function converts url to human readable filename. The algorithm
    is the simplest - all non-numbers and non-letters will be replaced
    with a default sign.

    Args:
        url (str): URL

    Return:

        file_name (str): string suitable for naming the file
    """

    lconfig = config.convert_url_to_filename
    file_name = ''
    for char in url:
        if char.isalpha() or char.isnumeric():
            file_name += char
        else:
            file_name += lconfig.get("delemiter", '')

    return file_name


def find_all_sources(html_text: str) -> list:
    """
    Function for finding links to resources on the given HTML page

    Args:
        html_test (str): text in HTML format

    Return:
        source_list (list): links to all resources found on the page
    """
    soup = BeautifulSoup(html_text, 'html.parser')

    source_list = []
    for tag in soup.find_all(('img', 'link', 'script')):
        if tag.name == 'img' and tag.has_attr('src'):
            source_list.append(tag.get('src'))
        elif tag.name == 'link' and tag.has_attr('href'):
            if not tag.has_attr('rel') or 'stylesheet' in tag.get('rel', []):
                source_list.append(tag.get('href'))
        elif tag.name == 'script' and tag.has_attr('src'):
            source_list.append(tag.get('src'))

    return source_list


def replace_all_sources(html_text: str, source_list: list) -> str:
    pass


def lokalize_source_links(source_list: list) -> list:
    pass


def download(url: str, output_dir: str = config.default_output_dir) -> bool:
    """
    The function downloads the source data with all loaded resources
    (pictures, javascript, css, etc.) and saves it to a local directory

    Args:
        url (str): URL page to download
        output_dir (str): path to the local directory where the result
            will be saved

    Return: True|False
    """
    logger = logging.getLogger()
    success = False

    try:
        logger.debug("Receiving data by address: {}".format(url))
        content = page_loader.fetcher.fetch_data_by_url(url)

        filename = ''.join((_convert_url_to_filename(url), '.html'))

        logger.debug(
            "Saving the received data into a file '{}' of the '{}' directory:"
            .format(filename, output_dir)
        )
        page_loader.keeper.save_source_locally(
            filename, output_dir, content)

        success = True
    except Exception as e:
        logger.error(e)
        success = False

    return success


def main():
    """
    The main function of launching the Application in the console
    """
    args = page_loader.cli.parse_arguments(__version__)

    log_level = args["log_level"]
    logging.basicConfig(filename="loader.log", level=log_level.upper())
    logger = logging.getLogger()

    logger.debug(
        """
            Application launch options:
                url: {}
                output: {}
                log_level: {}
        """.format(args["url"], args["output"], args["log_level"])
    )

    success = download(args["url"], args["output"])
    if success is True:
        logger.info("Url {} successfully saved".format(args["url"]))
        sys.exit(0)
    else:
        logger.error("Can't save Url {}".format(args["url"]))
        sys.exit(1)
