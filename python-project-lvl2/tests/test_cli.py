"""Automatic test to verify processing of command line arguments"""

import sys
import pytest
import gendiff.cli


def test_return_values():
    sys.argv = [
        'gendiff',
        './tests/fixtures/a.json',
        './tests/fixtures/b.json'
    ]
    args = gendiff.cli.parse_arguments()
    assert(
        isinstance(args, dict)
        and "format" in args
        and "filepath_1" in args
        and "filepath_2" in args
    )


def test_required_arguments():
    sys.argv = ['gendiff']
    with pytest.raises(SystemExit) as error:
        gendiff.cli.parse_arguments()
    assert error.value.code == 2
