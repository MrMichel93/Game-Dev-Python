"""Tests for Practice Problem 3: Function Composition"""
import pytest
import math
from practice_problem_3_starter import *


def test_apply_damage_with_armor():
    assert apply_damage_with_armor(100, 30, 10) == 80
    assert apply_damage_with_armor(100, 5, 10) >= 99  # Min 1 damage


def test_move_towards():
    x, y = move_towards(0, 0, 10, 0, 5)
    assert x == 5 and y == 0


def test_spawn_at_random_edge():
    for _ in range(10):
        x, y = spawn_at_random_edge(800, 600)
        at_edge = (x == 0 or x == 800 or y == 0 or y == 600)
        assert at_edge


def test_calculate_score_multiplier():
    assert calculate_score_multiplier(0, False) == 1.0
    assert calculate_score_multiplier(5, False) == 1.5
    assert calculate_score_multiplier(5, True) == 3.0


def test_create_projectile():
    proj = create_projectile(100, 200, 0, 10)
    assert 'x' in proj and 'y' in proj
    assert 'vx' in proj and 'vy' in proj


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
