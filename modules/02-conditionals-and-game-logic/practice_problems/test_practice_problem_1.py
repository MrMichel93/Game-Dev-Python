"""
Tests for Practice Problem 1: Boundary Checker
Run with: pytest test_practice_problem_1.py
"""

import pytest
from practice_problem_1_starter import (
    is_within_bounds,
    is_at_edge,
    clamp_to_bounds,
    get_quadrant,
    check_collision_circle
)


class TestIsWithinBounds:
    """Tests for is_within_bounds function"""
    
    def test_point_inside_bounds(self):
        """Test point clearly inside bounds"""
        assert is_within_bounds(100, 200, 800, 600) == True
        assert is_within_bounds(400, 300, 800, 600) == True
    
    def test_point_at_origin(self):
        """Test point at (0, 0)"""
        assert is_within_bounds(0, 0, 800, 600) == True
    
    def test_point_at_edge(self):
        """Test point at boundary edge"""
        assert is_within_bounds(799, 599, 800, 600) == True
        assert is_within_bounds(800, 600, 800, 600) == False
    
    def test_negative_coordinates(self):
        """Test negative coordinates"""
        assert is_within_bounds(-10, 200, 800, 600) == False
        assert is_within_bounds(100, -5, 800, 600) == False


class TestIsAtEdge:
    """Tests for is_at_edge function"""
    
    def test_near_left_edge(self):
        """Test point near left edge"""
        assert is_at_edge(5, 300, 800, 600, 10) == True
    
    def test_near_right_edge(self):
        """Test point near right edge"""
        assert is_at_edge(795, 300, 800, 600, 10) == True
    
    def test_near_top_edge(self):
        """Test point near top edge"""
        assert is_at_edge(400, 5, 800, 600, 10) == True
    
    def test_near_bottom_edge(self):
        """Test point near bottom edge"""
        assert is_at_edge(400, 595, 800, 600, 10) == True
    
    def test_center_point(self):
        """Test point in center (not near any edge)"""
        assert is_at_edge(400, 300, 800, 600, 10) == False


class TestClampToBounds:
    """Tests for clamp_to_bounds function"""
    
    def test_clamp_x_too_large(self):
        """Test clamping x coordinate that's too large"""
        assert clamp_to_bounds(900, 300, 800, 600) == (799, 300)
    
    def test_clamp_x_too_small(self):
        """Test clamping negative x coordinate"""
        assert clamp_to_bounds(-10, 300, 800, 600) == (0, 300)
    
    def test_clamp_y_too_large(self):
        """Test clamping y coordinate that's too large"""
        assert clamp_to_bounds(400, 700, 800, 600) == (400, 599)
    
    def test_clamp_y_too_small(self):
        """Test clamping negative y coordinate"""
        assert clamp_to_bounds(400, -20, 800, 600) == (400, 0)
    
    def test_clamp_both_coordinates(self):
        """Test clamping both coordinates"""
        assert clamp_to_bounds(900, 700, 800, 600) == (799, 599)
    
    def test_no_clamping_needed(self):
        """Test that valid coordinates are not changed"""
        assert clamp_to_bounds(400, 300, 800, 600) == (400, 300)


class TestGetQuadrant:
    """Tests for get_quadrant function"""
    
    def test_top_left(self):
        """Test top-left quadrant"""
        assert get_quadrant(100, 100, 800, 600) == "top-left"
        assert get_quadrant(0, 0, 800, 600) == "top-left"
    
    def test_top_right(self):
        """Test top-right quadrant"""
        assert get_quadrant(700, 100, 800, 600) == "top-right"
        assert get_quadrant(500, 200, 800, 600) == "top-right"
    
    def test_bottom_left(self):
        """Test bottom-left quadrant"""
        assert get_quadrant(100, 500, 800, 600) == "bottom-left"
        assert get_quadrant(300, 400, 800, 600) == "bottom-left"
    
    def test_bottom_right(self):
        """Test bottom-right quadrant"""
        assert get_quadrant(700, 500, 800, 600) == "bottom-right"
        assert get_quadrant(500, 400, 800, 600) == "bottom-right"


class TestCheckCollisionCircle:
    """Tests for check_collision_circle function"""
    
    def test_circles_touching(self):
        """Test circles that are just touching"""
        assert check_collision_circle(100, 100, 20, 140, 100, 20) == True
    
    def test_circles_overlapping(self):
        """Test circles that overlap"""
        assert check_collision_circle(100, 100, 20, 110, 100, 20) == True
    
    def test_circles_apart(self):
        """Test circles that are apart"""
        assert check_collision_circle(100, 100, 20, 200, 100, 20) == False
    
    def test_circles_same_center(self):
        """Test circles at same position"""
        assert check_collision_circle(100, 100, 20, 100, 100, 20) == True
    
    def test_different_sized_circles(self):
        """Test circles with different radii"""
        assert check_collision_circle(100, 100, 10, 130, 100, 30) == True
        assert check_collision_circle(100, 100, 10, 200, 100, 10) == False


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
