'''Automatic tests for core.py module'''

import os
import shutil
import page_loader.core


TEST_DIR = './tests/result'


def _remove_test_dir():
    if os.path.exists(TEST_DIR):
        shutil.rmtree(TEST_DIR)

    return True


def test_main():
    assert "main" in dir(page_loader.core)


def test_download():
    _remove_test_dir()
    success = page_loader.core.download('https://ya.ru/', TEST_DIR)

    assert(
        isinstance(success, bool)
        and success is True
        and os.path.exists(TEST_DIR)
    )
    _remove_test_dir()
