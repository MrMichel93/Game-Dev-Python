"""Tests for Practice Problem 2: Game Logic Functions"""
import pytest
from practice_problem_2_starter import *


def test_is_in_range():
    assert is_in_range(10, 12, 3) == True
    assert is_in_range(10, 20, 5) == False


def test_apply_gravity():
    assert apply_gravity(5) == 5.5
    assert apply_gravity(0, 1.0) == 1.0


def test_bounce_velocity():
    assert bounce_velocity(10) == -8.0
    assert bounce_velocity(-10, 0.5) == 5.0


def test_wrap_position():
    assert wrap_position(850, 800) == 50
    assert wrap_position(400, 800) == 400


def test_calculate_health_percentage():
    assert calculate_health_percentage(50, 100) == 50.0
    assert calculate_health_percentage(0, 100) == 0.0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
