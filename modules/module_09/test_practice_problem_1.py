"""Tests for Practice Problem 1: Game Balance Calculations"""
import pytest
from practice_problem_1_starter import *


def test_calculate_level_xp():
    assert calculate_level_xp(1) == 100
    assert calculate_level_xp(5) == 500


def test_calculate_enemy_health():
    assert calculate_enemy_health(1) == 150
    assert calculate_enemy_health(0) == 100


def test_calculate_drop_chance():
    assert calculate_drop_chance(0.5, 10) <= 0.95
    assert calculate_drop_chance(0.1, 0) == 0.1


def test_scale_reward():
    reward = scale_reward(100, 1.5)
    assert reward == 150


def test_calculate_damage_variance():
    for _ in range(10):
        damage = calculate_damage_variance(100)
        assert 90 <= damage <= 110


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
