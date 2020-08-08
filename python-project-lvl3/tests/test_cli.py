"""Automatic test to verify processing of command line arguments"""

import sys
import pytest
import page_loader.cli


def test_parse_arguments_return_values():
    sys.argv = [
        "page_loader",
        "https://ru.hexlet.io/"
    ]
    args = page_loader.cli.parse_arguments()
    assert(
        isinstance(args, dict)
        and "url" in args
        and "output" in args
        and "log_level" in args
    )


def test_required_arguments():
    sys.argv = ["page_loader"]
    with pytest.raises(SystemExit) as error:
        page_loader.cli.parse_arguments()
    assert error.value.code == 2
