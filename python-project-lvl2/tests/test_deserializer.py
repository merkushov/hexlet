"""
    Automated tests for the Deserialization mudule.
    The module reads the file and converts the file
    structure to data in the internal representation.
"""

import gendiff.deserializer


def test_json_read():
    data = gendiff.deserializer.process('./tests/fixtures/a.json')
    assert(isinstance(data, dict) and 'host' in data)


def test_yaml_read():
    data = gendiff.deserializer.process('./tests/fixtures/a.yaml')
    assert(isinstance(data, dict) and "host" in data)
