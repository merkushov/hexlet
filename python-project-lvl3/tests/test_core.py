'''Automatic tests for core.py module'''

import os
import page_loader.core
import page_loader.config as config
from tmpdir import TemporaryDirectory

TEST_DIR = config.tests['directory']


def test_main():
    assert "main" in dir(page_loader.core)


def test_download():
    with TemporaryDirectory(TEST_DIR):
        page_loader.core.download('https://ya.ru/', TEST_DIR)

        assert os.path.exists(TEST_DIR)
