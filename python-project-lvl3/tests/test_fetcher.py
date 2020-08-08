"""Automatic tests for fetcher.py module"""

import pytest
import page_loader.fetcher


def test_fetch_data_by_url():
    string = page_loader.fetcher.fetch_data_by_url("https://ya.ru/")

    assert(
        isinstance(string, str)
        and string.find("<body")
    )


def test_fetch_wrong_url():
    with pytest.raises(ConnectionError):
        page_loader.fetcher.fetch_data_by_url("fake")


def test_fetch_empty_url():
    with pytest.raises(ConnectionError):
        page_loader.fetcher.fetch_data_by_url("")


def test_fetch_404_url():
    with pytest.raises(ConnectionError):
        page_loader.fetcher.fetch_data_by_url("https://github.com/404")
