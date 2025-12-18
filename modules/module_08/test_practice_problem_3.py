"""Tests for Practice Problem 3: Collision Response"""
import pytest
from practice_problem_3_starter import *


def test_separate_circles():
    x1, y1, x2, y2 = separate_circles(0, 0, 10, 5, 0, 10)
    # Circles should be moved apart
    import math
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    assert distance >= 19  # Should be at least sum of radii


def test_reflect_velocity():
    # Reflect downward velocity off horizontal surface
    vx, vy = reflect_velocity(5, 10, 0, -1)
    assert vx == 5
    assert vy < 0  # Should bounce up


def test_is_moving_towards():
    # Moving right towards object on right
    assert is_moving_towards(0, 0, 5, 0, 10, 0) == True
    # Moving away
    assert is_moving_towards(0, 0, -5, 0, 10, 0) == False


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
