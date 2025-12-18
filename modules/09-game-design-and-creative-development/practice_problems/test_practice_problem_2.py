"""Tests for Practice Problem 2: Procedural Generation"""
import pytest
from practice_problem_2_starter import *


def test_generate_random_color():
    r, g, b = generate_random_color()
    assert 0 <= r <= 255
    assert 0 <= g <= 255
    assert 0 <= b <= 255


def test_generate_random_position():
    for _ in range(10):
        x, y = generate_random_position(800, 600, 50)
        assert 50 <= x <= 750
        assert 50 <= y <= 550


def test_generate_loot_table():
    loot = generate_loot_table(5)
    assert len(loot) == 5
    assert 'name' in loot[0]


def test_generate_wave_enemies():
    enemies = generate_wave_enemies(3)
    assert len(enemies) == 6  # wave * 2


def test_shuffle_deck():
    original = [1, 2, 3, 4, 5]
    shuffled = shuffle_deck(original)
    assert len(shuffled) == len(original)
    assert set(shuffled) == set(original)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
