'''Automatic tests for core.py module'''

import page_loader.core


def test_main():
    assert "main" in dir(page_loader.core)
