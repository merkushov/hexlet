"""Automatic tests for core.py module"""

import os
import pytest
import page_loader.core
import page_loader.config as config
from tmpdir import TemporaryDirectory

TEST_DIR = config.tests["directory"]


def test_main():
    assert "main" in dir(page_loader.core)


def test_download():
    with TemporaryDirectory(TEST_DIR):
        page_loader.core.download("https://ya.ru/", TEST_DIR)

        assert os.path.exists(TEST_DIR)


@pytest.mark.parametrize(
    "url,expected_file_name", [
        (
            "https://hexlet.io/",
            "https___hexlet_io_"
        ),
        (
            "http://ya.ru/search?query=hexlet;l=",
            "http___ya_ru_search_query_hexlet_l_",
        ),
        (
            "123_123_abc",
            "123_123_abc",
        )
    ]
)
def test_convert_url_to_filename(url, expected_file_name):
    assert expected_file_name == page_loader.core._convert_url_to_filename(url)
