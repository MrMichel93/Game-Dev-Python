"""Tests for Practice Problem 1: Collision Detection Basics"""
import pytest
from practice_problem_1_starter import *


def test_check_circle_collision():
    assert check_circle_collision(0, 0, 10, 15, 0, 10) == True
    assert check_circle_collision(0, 0, 10, 50, 0, 10) == False


def test_check_rect_collision():
    assert check_rect_collision(0, 0, 50, 50, 25, 25, 50, 50) == True
    assert check_rect_collision(0, 0, 50, 50, 100, 100, 50, 50) == False


def test_check_point_circle_collision():
    assert check_point_circle_collision(5, 5, 0, 0, 10) == True
    assert check_point_circle_collision(50, 50, 0, 0, 10) == False


def test_check_point_rect_collision():
    assert check_point_rect_collision(25, 25, 0, 0, 50, 50) == True
    assert check_point_rect_collision(75, 75, 0, 0, 50, 50) == False


def test_get_collision_depth():
    depth = get_collision_depth(0, 0, 10, 15, 0, 10)
    assert depth == 5  # (10+10) - 15


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
