"""Tests for Practice Problem 2: Nested Dictionaries"""
import pytest
from practice_problem_2_starter import *


def test_create_game_state():
    state = create_game_state(1, 0, "Hero")
    assert state['level'] == 1
    assert 'player' in state


def test_get_nested_value():
    data = {'a': {'b': {'c': 42}}}
    assert get_nested_value(data, ['a', 'b', 'c']) == 42


def test_merge_dicts():
    d1 = {'a': 1, 'b': 2}
    d2 = {'b': 3, 'c': 4}
    result = merge_dicts(d1, d2)
    assert result['b'] == 3
    assert result['c'] == 4


def test_count_dict_keys():
    data = {'a': 1, 'b': {'c': 2, 'd': 3}}
    count = count_dict_keys(data)
    assert count >= 4  # a, b, c, d


def test_flatten_dict():
    data = {'a': {'b': 1}}
    flat = flatten_dict(data)
    assert 'a_b' in flat


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
