"""Tests for Practice Problem 2: Accessibility Features"""
import pytest
from practice_problem_2_starter import *


def test_adjust_volume():
    assert adjust_volume(50, 10) == 60
    assert adjust_volume(95, 10) == 100  # Capped
    assert adjust_volume(5, -10) == 0  # Capped


def test_get_contrast_color():
    white = get_contrast_color(0, 0, 0)  # Black bg needs white
    assert white == (255, 255, 255)
    black = get_contrast_color(255, 255, 255)  # White bg needs black
    assert black == (0, 0, 0)


def test_scale_ui_size():
    assert scale_ui_size(10, 1.5) == 15
    assert scale_ui_size(20, 2.0) == 40


def test_convert_to_colorblind_safe():
    safe_color = convert_to_colorblind_safe("red")
    assert safe_color is not None


def test_generate_text_to_speech():
    text = generate_text_to_speech("Hello! How are you?")
    assert isinstance(text, str)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
