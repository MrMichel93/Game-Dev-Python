"""Tests for Practice Problem 2: Physics Calculations"""
import pytest
import math
from practice_problem_2_starter import *


def test_apply_velocity():
    x, y = apply_velocity(10, 20, 5, 3)
    assert x == 15 and y == 23


def test_apply_friction():
    vx, vy = apply_friction(10, 10, 0.9)
    assert vx == 9 and vy == 9


def test_calculate_bounce():
    assert calculate_bounce(10, 0.8) == -8


def test_apply_acceleration():
    vx, vy = apply_acceleration(5, 5, 2, 1)
    assert vx == 7 and vy == 6


def test_limit_velocity():
    vx, vy = limit_velocity(10, 10, 5)
    mag = math.sqrt(vx*vx + vy*vy)
    assert mag <= 5.1  # Allow small floating point error


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
