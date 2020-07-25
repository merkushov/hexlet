"""
    Automatic tests for the Serialization mudule.
    A module is an interface to other serialization modules.
"""

import pytest
import gendiff.serializer


def test_json_serialization():
    data = {'a': 1, 'b': 2}

    result_data = gendiff.serializer.process(data, 'json')
    assert(
        isinstance(result_data, str)
    )


def test_dictionary_serialization():
    data = {"a": ["changed", ["1", "2"]]}

    result_data = gendiff.serializer.process(data, 'dictionary')
    assert(
        isinstance(result_data, str)
    )


def test_plain_serialization():
    data = {"a": ["changed", ["1", "2"]]}

    result_data = gendiff.serializer.process(data, 'plain')
    assert(
        isinstance(result_data, str)
    )


def test_wrong_output_format():
    data = {"a": 1}

    with pytest.raises(Exception) as error:
        gendiff.serializer.process(data, 'fake')
    assert(error and error.value)
