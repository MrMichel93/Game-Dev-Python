"""Tests for Practice Problem 1: Input State Management"""
import pytest
from practice_problem_1_starter import *


def test_create_input_state():
    state = create_input_state()
    assert state['up'] == False
    assert state['space'] == False


def test_update_key_state():
    state = create_input_state()
    update_key_state(state, 'up', True)
    assert state['up'] == True


def test_is_key_pressed():
    state = {'up': True, 'down': False}
    assert is_key_pressed(state, 'up') == True
    assert is_key_pressed(state, 'down') == False


def test_get_movement_direction():
    state = {'up': True, 'down': False, 'left': False, 'right': True}
    dx, dy = get_movement_direction(state)
    assert dx == 1  # right
    assert dy == -1  # up


def test_any_key_pressed():
    state = {'up': False, 'down': False, 'left': True}
    assert any_key_pressed(state) == True
    state = {'up': False, 'down': False}
    assert any_key_pressed(state) == False


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
