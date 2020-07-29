"""
    Automatic Unit tests for the Plain Serialization mudule.
    The module takes the internal representation data
    and convert them into strings
"""

import pytest
import gendiff.serializers.plain


@pytest.mark.parametrize(
    'data,success_string', [
        (
            {"a": ["changed", ["1", "2"]]},
            'Setting "a" changed from "1" to "2".\n'
        ),
        (
            {"b": ["added", "new"]},
            'Setting "b" added with value "new".\n'
        ),
        (
            {"c": ["removed", "old"]},
            'Setting "c" deleted.\n'
        ),
        (
            {"d": ["equal", 55]},
            ''
        ),
        (
            {"n": ["nested", {"a": ["added", "new"]}]},
            'Setting "n.a" added with value "new".\n'
        ),
        (
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
        ),
        (
            {"nd": ["nested", {"n": ["nested", {"d": ["removed", "old"]}]}]},
            'Setting "nd.n.d" deleted.\n'
        ),
        (
            {
                "n": ["nested", {"a": ["added", "my"]}],
                "b": ["changed", ["foo", "bar"]],
                "eq": ["equal", "abc"]
            },
            'Setting "b" changed from "foo" to "bar".\n'
            + 'Setting "n.a" added with value "my".\n'
        )
    ]
)
def test_process(data, success_string):
    result_str = gendiff.serializers.plain.process(data)
    assert(
        isinstance(result_str, str)
        and result_str == success_string
    )
