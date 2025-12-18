"""Tests for Practice Problem 3: Dictionary Transformations"""
import pytest
from practice_problem_3_starter import *


def test_filter_by_value():
    data = {'a': 10, 'b': 5, 'c': 20}
    result = filter_by_value(data, 10)
    assert 'a' in result and 'c' in result
    assert 'b' not in result


def test_invert_dict():
    data = {'a': 1, 'b': 2}
    result = invert_dict(data)
    assert result[1] == 'a'
    assert result[2] == 'b'


def test_get_dict_keys_sorted():
    data = {'c': 1, 'a': 2, 'b': 3}
    keys = get_dict_keys_sorted(data)
    assert keys == ['a', 'b', 'c']


def test_dict_to_list_of_tuples():
    data = {'a': 1, 'b': 2}
    result = dict_to_list_of_tuples(data)
    assert ('a', 1) in result
    assert ('b', 2) in result


def test_group_by_value():
    data = {'a': 1, 'b': 1, 'c': 2}
    result = group_by_value(data)
    assert 'a' in result[1] and 'b' in result[1]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
