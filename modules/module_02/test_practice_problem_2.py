"""
Tests for Practice Problem 2: Collision Detection
Run with: pytest test_practice_problem_2.py

Note: This tests the FIXED version of practice problem 2.
Students should fix practice_problem_2_buggy.py to match practice_problem_2_fixed.py
"""

import pytest


def test_fixed_version_exists():
    """Test that the fixed version exists"""
    try:
        import practice_problem_2_fixed
        assert True
    except ImportError:
        pytest.fail("practice_problem_2_fixed.py should exist")


def test_fixed_has_all_variables():
    """Test that all required variables exist"""
    from practice_problem_2_fixed import (
        player_x, player_y, player_size,
        enemy_x, enemy_y, enemy_size,
        collision_detected
    )
    
    assert isinstance(player_x, (int, float))
    assert isinstance(player_y, (int, float))
    assert isinstance(player_size, (int, float))
    assert isinstance(enemy_x, (int, float))
    assert isinstance(enemy_y, (int, float))
    assert isinstance(enemy_size, (int, float))
    assert isinstance(collision_detected, bool)


def test_fixed_functions_exist():
    """Test that draw and update functions exist"""
    import practice_problem_2_fixed
    
    assert hasattr(practice_problem_2_fixed, 'draw')
    assert hasattr(practice_problem_2_fixed, 'update')
    assert callable(practice_problem_2_fixed.draw)
    assert callable(practice_problem_2_fixed.update)


def test_buggy_version_has_bugs():
    """Test that buggy version can be imported (has syntax-valid bugs)"""
    try:
        import practice_problem_2_buggy
        # Buggy version should import without syntax errors
        assert hasattr(practice_problem_2_buggy, 'draw')
        assert hasattr(practice_problem_2_buggy, 'update')
    except ImportError:
        pytest.fail("practice_problem_2_buggy.py should be importable")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
