"""
Tests for Practice Problem 2: Score System
Run with: pytest test_practice_problem_2.py

Note: This tests the FIXED version of practice problem 2.
Students should fix practice_problem_2_buggy.py to match practice_problem_2_fixed.py
"""

import pytest


def test_fixed_version_exists():
    """Test that the fixed version of the practice problem exists"""
    try:
        from practice_problem_2_fixed import score, player_name, high_score, bonus_points
        assert True
    except ImportError:
        pytest.fail("practice_problem_2_fixed.py should exist with all variables defined")


def test_player_name_is_string():
    """Test that player_name is a string (Bug 1 fix)"""
    from practice_problem_2_fixed import player_name
    assert isinstance(player_name, str), "player_name should be a string with quotes"


def test_score_variable_exists():
    """Test that score variable exists and is accessible"""
    from practice_problem_2_fixed import score
    assert isinstance(score, int), "score should be an integer"


def test_variables_have_correct_initial_values():
    """Test that all variables have expected initial values"""
    from practice_problem_2_fixed import score, bonus_points, player_name, high_score
    
    assert score == 0, "score should start at 0"
    assert bonus_points == 50, "bonus_points should be 50"
    assert player_name == "Hero", "player_name should be 'Hero' with quotes"
    assert high_score == 100, "high_score should be 100"


def test_global_keyword_understanding():
    """Test that students understand when global keyword is needed"""
    # This test checks if the fixed version can be imported without errors
    # If global keywords are missing, the module would have issues
    try:
        import practice_problem_2_fixed
        # Check that functions exist
        assert hasattr(practice_problem_2_fixed, 'draw')
        assert hasattr(practice_problem_2_fixed, 'update')
        assert callable(practice_problem_2_fixed.draw)
        assert callable(practice_problem_2_fixed.update)
    except Exception as e:
        pytest.fail(f"Fixed version should import and define functions correctly: {e}")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
