'''Automatic tests for fetcher.py module'''

import page_loader.fetcher


def test_fetch_data_by_url():
    string = page_loader.fetcher.fetch_data_by_url('https://ya.ru/')

    assert(
        isinstance(string, str)
        and string.find('<body')
    )
