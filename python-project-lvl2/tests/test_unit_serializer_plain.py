"""
    Automatic Unit tests for the Plain Serialization mudule.
    The module takes the internal representation data
    and convert them into strings
"""

import gendiff.serializers.plain


def _check(data, success_string):
    result_str = gendiff.serializers.plain.process(data)
    assert(
        isinstance(result_str, str)
        and result_str == success_string
    )


def test_process_changed():
    _check(
        {"a": ["changed", ["1", "2"]]},
        'Setting "a" changed from "1" to "2".\n'
    )


def test_process_added():
    _check(
        {"b": ["added", "new"]},
        'Setting "b" added with value "new".\n'
    )


def test_process_removed():
    _check(
        {"c": ["removed", "old"]},
        'Setting "c" deleted.\n'
    )


def test_process_equal():
    _check(
        {"d": ["equal", 55]},
        ''
    )


def test_process_nested_added():
    _check(
        {"n": ["nested", {"a": ["added", "new"]}]},
        'Setting "n.a" added with value "new".\n'
    )


def test_process_nested_deep_changed():
    _check(
        {
            "nd": [
                "nested",
                {
                    "n": [
                        "nested",
                        {
                            "c": [
                                "changed",
                                ["4", "abc"]
                            ]
                        }
                    ]
                }
            ]
        },
        'Setting "nd.n.c" changed from "4" to "abc".\n'
    )


def test_process_nested_deep_removed():
    _check(
        {"nd": ["nested", {"n": ["nested", {"d": ["removed", "old"]}]}]},
        'Setting "nd.n.d" deleted.\n'
    )


def test_process_multiple_actions():
    _check(
        {
            "n": ["nested", {"a": ["added", "my"]}],
            "b": ["changed", ["foo", "bar"]],
            "eq": ["equal", "abc"]
        },
        'Setting "b" changed from "foo" to "bar".\n'
        + 'Setting "n.a" added with value "my".\n'
    )
