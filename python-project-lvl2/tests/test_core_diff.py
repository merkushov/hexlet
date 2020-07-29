'''Automatic test to check data comparision algorithm'''

import gendiff.core


def test_diff_between_data_changed():
    d1 = {'a': 1, 'b': 2}
    d2 = {'a': 2}

    result_data = gendiff.core.diff_between_data(d1, d2)
    assert(
        isinstance(result_data, dict)
        and result_data['a']
        and result_data['a'][0] == 'changed'
        and result_data['a'][1] == (1, 2)
    )


def test_diff_between_data_removed():
    d1 = {'a': 1, 'b': 2}
    d2 = {'a': 1, 'c': 3}

    res = gendiff.core.diff_between_data(d1, d2)
    assert(
        isinstance(res, dict)
        and res['b']
        and res['b'][0] == 'removed'
        and res['b'][1] == 2
    )


def test_diff_between_data_added():
    d1 = {'a': 1, 'b': 2}
    d2 = {'a': 1, 'c': 3}

    res = gendiff.core.diff_between_data(d1, d2)
    assert(
        isinstance(res, dict)
        and res['c']
        and res['c'][0] == 'added'
        and res['c'][1] == 3
    )


def test_diff_between_data_equal():
    d1 = {"a": 1, "b": 2}
    d2 = {"a": 1}

    res = gendiff.core.diff_between_data(d1, d2)
    assert(
        isinstance(res, dict)
        and res['a']
        and res['a'][0] == 'equal'
        and res['a'][1] == 1
    )


def test_diff_between_data_nested():
    d1 = {'a': {'b': 2}, 'c': {'d': 4}}
    d2 = {'a': {'b': 2}, 'c': {'d': 5}}

    res = gendiff.core.diff_between_data(d1, d2)
    assert(
        isinstance(res, dict)
        and res['a']
        and res['a'][0] == 'nested'
        and res['c']
        and res['c'][0] == 'nested'
    )
