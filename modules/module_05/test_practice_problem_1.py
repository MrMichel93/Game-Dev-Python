"""Tests for Practice Problem 1: Basic Functions"""
import pytest
import math
from practice_problem_1_starter import *


def test_calculate_distance():
    assert calculate_distance(0, 0, 3, 4) == 5.0
    assert calculate_distance(0, 0, 0, 0) == 0.0


def test_clamp_value():
    assert clamp_value(5, 0, 10) == 5
    assert clamp_value(-5, 0, 10) == 0
    assert clamp_value(15, 0, 10) == 10


def test_lerp():
    assert lerp(0, 10, 0.5) == 5.0
    assert lerp(0, 10, 0) == 0
    assert lerp(0, 10, 1) == 10


def test_calculate_angle():
    angle = calculate_angle(0, 0, 1, 0)
    assert abs(angle - 0) < 0.1
    angle = calculate_angle(0, 0, 0, 1)
    assert abs(angle - 90) < 0.1


def test_normalize_vector():
    x, y = normalize_vector(3, 4)
    magnitude = math.sqrt(x*x + y*y)
    assert abs(magnitude - 1.0) < 0.01


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
