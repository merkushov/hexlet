"""
    Automatic integration tests. They check the entire chain of actions:
      - reading files
      - content comparison
      - result formatting
"""

import pytest
import gendiff.engine

FPATH = './tests/fixtures/'


def _make_path(filename):
    return '{}{}'.format(FPATH, filename)


@pytest.mark.parametrize(
    'file1,file2,output_format,output_file', [
        (
            'case1_before.json',
            'case1_after.json',
            'json',
            'case1_expected_json.txt'
        ),
        (
            'case1_before.json',
            'case1_after.json',
            'plain',
            'case1_expected_plain.txt'
        ),
        (
            'case1_before.json',
            'case1_after.json',
            'dictionary',
            'case1_expected_dictionary.txt'
        ),
        (
            'case1_before.yaml',
            'case1_after.yaml',
            'json',
            'case1_expected_json.txt'
        ),
        (
            'case1_before.yaml',
            'case1_after.yaml',
            'plain',
            'case1_expected_plain.txt'
        ),
        (
            'case1_before.yaml',
            'case1_after.yaml',
            'dictionary',
            'case1_expected_dictionary.txt'
        ),
    ],
)
def test_comparison(file1, file2, output_format, output_file):
    expected_text = ''
    with open(_make_path(output_file), 'r') as file_object:
        expected_text = file_object.read()

    diff_data = gendiff.engine.diff_between_files(
        _make_path(file1), _make_path(file2)
    )
    diff_text = gendiff.engine.format(diff_data, output_format)

    assert diff_text == expected_text
