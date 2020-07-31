"""
    Automated tests for the Deserialization mudule.
    The module reads the file and converts the file
    structure to data in the internal representation.
"""

import pytest
import gendiff.deserializer


def test_json_read():
    data = gendiff.deserializer.process('./tests/fixtures/a.json')
    assert(isinstance(data, dict) and 'host' in data)


def test_yaml_read():
    data = gendiff.deserializer.process('./tests/fixtures/a.yaml')
    assert(isinstance(data, dict) and "host" in data)


@pytest.mark.parametrize(
    'filepath', [
        # wrong extenstion
        ('Makefile'),

        # wrong file structure
        ('./tests/fixtures/empty.json'),
        ('./tests/fixtures/wrong.yaml'),

        # non-existent file
        ('fake.json'),
        ('fake.yml'),
    ]
)
def test_wrong_format(filepath):
    with pytest.raises(Exception) as error:
        gendiff.deserializer.process(filepath)
    assert(error and error.value)
