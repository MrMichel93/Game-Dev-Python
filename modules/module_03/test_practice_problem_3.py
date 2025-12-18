"""
Tests for Practice Problem 3: Animation Helpers
Run with: pytest test_practice_problem_3.py
"""

import pytest
import math
from practice_problem_3_starter import (
    interpolate,
    fade_values,
    bounce_sequence,
    spiral_positions,
    flash_pattern
)


class TestInterpolate:
    """Tests for interpolate function"""
    
    def test_simple_interpolation(self):
        """Test simple interpolation"""
        result = interpolate(0, 10, 3)
        assert result == [0.0, 5.0, 10.0]
    
    def test_larger_range(self):
        """Test larger range"""
        result = interpolate(100, 200, 5)
        assert result == [100.0, 125.0, 150.0, 175.0, 200.0]
    
    def test_two_steps(self):
        """Test with just start and end"""
        result = interpolate(0, 100, 2)
        assert result == [0.0, 100.0]


class TestFadeValues:
    """Tests for fade_values function"""
    
    def test_fade_from_255(self):
        """Test fading from full opacity"""
        result = fade_values(255, 5)
        expected = [255, 204, 153, 102, 51]
        assert result == expected
    
    def test_fade_from_100(self):
        """Test fading from 100"""
        result = fade_values(100, 4)
        assert len(result) == 4
        assert result[0] == 100
        assert result[-1] < result[0]
    
    def test_correct_length(self):
        """Test correct number of values"""
        result = fade_values(200, 10)
        assert len(result) == 10


class TestBounceSequence:
    """Tests for bounce_sequence function"""
    
    def test_three_bounces(self):
        """Test three bounces"""
        result = bounce_sequence(100, 3)
        assert result == [100, 70, 49]
    
    def test_first_bounce_is_full_height(self):
        """Test first bounce is at full height"""
        result = bounce_sequence(150, 1)
        assert result[0] == 150
    
    def test_correct_number_of_bounces(self):
        """Test correct number of bounces"""
        result = bounce_sequence(100, 5)
        assert len(result) == 5


class TestSpiralPositions:
    """Tests for spiral_positions function"""
    
    def test_generates_correct_count(self):
        """Test correct number of positions"""
        result = spiral_positions(100, 100, 50, 4)
        assert len(result) == 4
    
    def test_returns_tuples(self):
        """Test returns tuples"""
        result = spiral_positions(100, 100, 50, 2)
        assert isinstance(result[0], tuple)
        assert len(result[0]) == 2
    
    def test_positions_around_center(self):
        """Test positions are around center"""
        result = spiral_positions(200, 200, 50, 8)
        # All positions should be within reasonable distance of center
        for x, y in result:
            distance = math.sqrt((x - 200)**2 + (y - 200)**2)
            assert distance <= 50  # Within starting radius


class TestFlashPattern:
    """Tests for flash_pattern function"""
    
    def test_alternating_pattern(self):
        """Test alternating flash pattern"""
        result = flash_pattern(10, 2)
        expected = [True, True, False, False, True, True, False, False, True, True]
        assert result == expected
    
    def test_single_frame_flash(self):
        """Test single frame flashing"""
        result = flash_pattern(6, 1)
        expected = [True, False, True, False, True, False]
        assert result == expected
    
    def test_correct_length(self):
        """Test correct total frames"""
        result = flash_pattern(15, 3)
        assert len(result) == 15


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
