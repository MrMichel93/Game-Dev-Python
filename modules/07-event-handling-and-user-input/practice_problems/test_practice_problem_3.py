"""Tests for Practice Problem 3: Mouse Input Handling"""
import pytest
from practice_problem_3_starter import *


def test_is_point_in_rect():
    assert is_point_in_rect(50, 50, 0, 0, 100, 100) == True
    assert is_point_in_rect(150, 50, 0, 0, 100, 100) == False


def test_calculate_mouse_offset():
    dx, dy = calculate_mouse_offset(100, 150, 50, 50)
    assert dx == 50 and dy == 100


def test_is_click_on_button():
    button = {'x': 0, 'y': 0, 'width': 100, 'height': 50}
    assert is_click_on_button(50, 25, button) == True
    assert is_click_on_button(150, 25, button) == False


def test_get_angle_to_mouse():
    angle = get_angle_to_mouse(0, 0, 1, 0)
    assert abs(angle - 0) < 1


def test_snap_to_grid():
    x, y = snap_to_grid(47, 53, 50)
    assert x == 50 and y == 50


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
