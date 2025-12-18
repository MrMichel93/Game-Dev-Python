"""Tests for Practice Problem 1: List Operations"""
import pytest
from practice_problem_1_starter import *


def test_add_item():
    inv = []
    add_item_to_inventory(inv, "sword")
    assert "sword" in inv
    add_item_to_inventory(inv, "shield")
    assert len(inv) == 2


def test_remove_item_exists():
    inv = ["sword", "shield", "potion"]
    assert remove_item_from_inventory(inv, "sword") == True
    assert "sword" not in inv
    assert len(inv) == 2


def test_remove_item_not_exists():
    inv = ["sword"]
    assert remove_item_from_inventory(inv, "hammer") == False
    assert len(inv) == 1


def test_get_item_valid_index():
    inv = ["a", "b", "c"]
    assert get_item_at_index(inv, 0) == "a"
    assert get_item_at_index(inv, 1) == "b"
    assert get_item_at_index(inv, 2) == "c"


def test_get_item_invalid_index():
    inv = ["a", "b"]
    assert get_item_at_index(inv, 10) is None
    assert get_item_at_index(inv, -10) is None


def test_count_item():
    inv = ["coin", "coin", "gem", "coin"]
    assert count_item(inv, "coin") == 3
    assert count_item(inv, "gem") == 1
    assert count_item(inv, "ruby") == 0


def test_merge_inventories():
    inv1 = ["a", "b"]
    inv2 = ["c", "d"]
    result = merge_inventories(inv1, inv2)
    assert len(result) == 4
    assert "a" in result and "d" in result


def test_get_unique_items():
    inv = ["coin", "gem", "coin", "sword", "gem"]
    unique = get_unique_items(inv)
    assert len(unique) == 3
    assert "coin" in unique
    assert "gem" in unique
    assert "sword" in unique


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
