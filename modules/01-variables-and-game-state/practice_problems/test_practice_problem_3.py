"""
Tests for Practice Problem 3: Health System
Run with: pytest test_practice_problem_3.py

Note: This tests the SOLUTION version (students extend the starter).
"""

import pytest


def test_solution_has_armor_variable():
    """Test that armor variable is added"""
    from practice_problem_3_solution import armor
    assert armor == 50, "armor should start at 50"


def test_solution_has_shield_variable():
    """Test that shield_active variable is added"""
    from practice_problem_3_solution import shield_active
    assert shield_active == True, "shield_active should start as True"


def test_solution_has_required_variables():
    """Test that all required variables exist"""
    from practice_problem_3_solution import (
        player_health,
        max_health,
        armor,
        shield_active
    )
    
    assert player_health == 100
    assert max_health == 100
    assert armor == 50
    assert shield_active == True


def test_solution_functions_exist():
    """Test that draw and update functions exist"""
    import practice_problem_3_solution
    
    assert hasattr(practice_problem_3_solution, 'draw')
    assert hasattr(practice_problem_3_solution, 'update')
    assert callable(practice_problem_3_solution.draw)
    assert callable(practice_problem_3_solution.update)


def test_starter_has_basic_variables():
    """Test that starter code has the basic variables"""
    from practice_problem_3_starter import player_health, max_health
    
    assert player_health == 100
    assert max_health == 100


def test_starter_functions_exist():
    """Test that starter code has draw and update functions"""
    import practice_problem_3_starter
    
    assert hasattr(practice_problem_3_starter, 'draw')
    assert hasattr(practice_problem_3_starter, 'update')


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
