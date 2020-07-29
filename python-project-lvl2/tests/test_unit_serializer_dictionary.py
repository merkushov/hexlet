"""
    Automatic Unit tests for the Dictionary Serialization module.
    The module takes the internal representation data
    and convert them into strings.
"""

import pytest
import gendiff.serializers.dictionary


@pytest.mark.parametrize(
    'data,success_string', [
        (
            {"a": ["added", "new"]},
            '{\n  + "a":new,\n}\n'
        ),
        (
            {"a": ["changed", ["1", "2"]]},
            '{\n  - "a":1,\n  + "a":2,\n}\n'
        ),
        (
            {"d": ["equal", 55]},
            '{\n    "d":55,\n}\n'
        ),
        (
            {"c": ["removed", "old"]},
            '{\n  - "c":old,\n}\n'
        ),
        (
            {"n": ["nested", {"a": ["added", "new"]}]},
            '{\n    "n":{\n      + "a":new,\n    }\n}\n'
        ),
        (
            {
                "n": ["nested", {"a": ["added", "my"]}],
                "b": ["changed", ["foo", "bar"]],
                "eq": ["equal", "abc"]
            },
            '{\n  - "b":foo,\n  + "b":bar,\n    '
            + '"eq":abc,\n    "n":{\n      + "a":my,\n    }\n}\n'
        )
    ]
)
def test_process(data, success_string):
    result_str = gendiff.serializers.dictionary.process(data)
    assert(
        isinstance(result_str, str)
        and result_str == success_string
    )
