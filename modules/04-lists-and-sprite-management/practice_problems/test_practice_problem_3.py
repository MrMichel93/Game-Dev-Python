"""Tests for Practice Problem 3: List Slicing"""
import pytest
from practice_problem_3_starter import *


def test_get_first_n_items():
    items = [1, 2, 3, 4, 5]
    assert get_first_n_items(items, 3) == [1, 2, 3]
    assert get_first_n_items(items, 0) == []


def test_get_last_n_items():
    items = [1, 2, 3, 4, 5]
    assert get_last_n_items(items, 2) == [4, 5]
    assert get_last_n_items(items, 1) == [5]


def test_get_every_nth_item():
    items = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert get_every_nth_item(items, 2) == [0, 2, 4, 6, 8]
    assert get_every_nth_item(items, 3) == [0, 3, 6, 9]


def test_reverse_list():
    items = [1, 2, 3, 4, 5]
    assert reverse_list(items) == [5, 4, 3, 2, 1]


def test_split_list():
    items = [1, 2, 3, 4, 5]
    left, right = split_list(items, 3)
    assert left == [1, 2, 3]
    assert right == [4, 5]


def test_rotate_list():
    items = [1, 2, 3, 4, 5]
    assert rotate_list(items, 2) == [4, 5, 1, 2, 3]
    assert rotate_list(items, -2) == [3, 4, 5, 1, 2]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
