"""
    Automatic Unit tests for the Dictionary Serialization module.
    The module takes the internal representation data
    and convert them into strings.
"""

import gendiff.serializers.dictionary


def _check(data, success_string):
    result_str = gendiff.serializers.dictionary.process(data)
    assert(
        isinstance(result_str, str)
        and result_str == success_string
    )


def test_process_added():
    _check(
        {"a": ["added", "new"]},
        '{\n  + "a":new,\n}\n'
    )


def test_process_changed():
    _check(
        {"a": ["changed", ["1", "2"]]},
        '{\n  - "a":1,\n  + "a":2,\n}\n'
    )


def test_process_equal():
    _check(
        {"d": ["equal", 55]},
        '{\n    "d":55,\n}\n'
    )


def test_process_removed():
    _check(
        {"c": ["removed", "old"]},
        '{\n  - "c":old,\n}\n'
    )


def test_process_nested_added():
    _check(
        {"n": ["nested", {"a": ["added", "new"]}]},
        '{\n    "n":{\n      + "a":new,\n    }\n}\n'
    )


def test_process_multiple_actions():
    _check(
        {
            "n": ["nested", {"a": ["added", "my"]}],
            "b": ["changed", ["foo", "bar"]],
            "eq": ["equal", "abc"]
        },
        '{\n  - "b":foo,\n  + "b":bar,\n    '
        + '"eq":abc,\n    "n":{\n      + "a":my,\n    }\n}\n'
    )
