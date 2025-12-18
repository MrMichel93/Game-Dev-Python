"""Tests for Practice Problem 3: Game State Patterns"""
import pytest
from practice_problem_3_starter import *


def test_implement_cooldown():
    assert implement_cooldown(0, 10, 5) == True
    assert implement_cooldown(8, 10, 5) == False


def test_calculate_combo_bonus():
    assert calculate_combo_bonus(0) == 1.0
    assert calculate_combo_bonus(5) == 1.5


def test_check_achievement():
    stats = {'kills': 100, 'score': 1000}
    req = {'kills': 50, 'score': 500}
    assert check_achievement(stats, req) == True


def test_calculate_star_rating():
    thresholds = [100, 200, 300, 400]
    assert calculate_star_rating(250, thresholds) == 2
    assert calculate_star_rating(500, thresholds) == 4


def test_create_save_data():
    save = create_save_data({'name': 'Hero'}, 5, ['sword'])
    assert 'player' in save
    assert 'level' in save


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
