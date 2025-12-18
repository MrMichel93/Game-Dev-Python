"""
Tests for Practice Problem 3: Game State Validator
Run with: pytest test_practice_problem_3.py
"""

import pytest
from practice_problem_3_starter import (
    can_level_up,
    get_difficulty_level,
    is_game_over,
    should_spawn_powerup,
    get_rank,
    calculate_bonus
)


class TestCanLevelUp:
    """Tests for can_level_up function"""
    
    def test_can_level_up_true(self):
        """Test when player can level up"""
        assert can_level_up(1500, 1) == True
        assert can_level_up(2000, 2) == True
    
    def test_can_level_up_false(self):
        """Test when player cannot level up"""
        assert can_level_up(500, 2) == False
        assert can_level_up(900, 1) == False
    
    def test_exact_threshold(self):
        """Test at exact level up threshold"""
        assert can_level_up(1000, 1) == True
        assert can_level_up(3000, 3) == True


class TestGetDifficultyLevel:
    """Tests for get_difficulty_level function"""
    
    def test_easy_difficulty(self):
        """Test easy difficulty range"""
        assert get_difficulty_level(0) == "Easy"
        assert get_difficulty_level(50) == "Easy"
        assert get_difficulty_level(99) == "Easy"
    
    def test_medium_difficulty(self):
        """Test medium difficulty range"""
        assert get_difficulty_level(100) == "Medium"
        assert get_difficulty_level(250) == "Medium"
        assert get_difficulty_level(499) == "Medium"
    
    def test_hard_difficulty(self):
        """Test hard difficulty range"""
        assert get_difficulty_level(500) == "Hard"
        assert get_difficulty_level(750) == "Hard"
        assert get_difficulty_level(999) == "Hard"
    
    def test_expert_difficulty(self):
        """Test expert difficulty range"""
        assert get_difficulty_level(1000) == "Expert"
        assert get_difficulty_level(5000) == "Expert"


class TestIsGameOver:
    """Tests for is_game_over function"""
    
    def test_game_over_no_lives(self):
        """Test game over when lives are 0"""
        assert is_game_over(0, 50) == True
    
    def test_game_over_no_health(self):
        """Test game over when health is 0"""
        assert is_game_over(3, 0) == True
    
    def test_game_over_both_zero(self):
        """Test game over when both are 0"""
        assert is_game_over(0, 0) == True
    
    def test_game_not_over(self):
        """Test game continues with positive values"""
        assert is_game_over(3, 50) == False
        assert is_game_over(1, 1) == False


class TestShouldSpawnPowerup:
    """Tests for should_spawn_powerup function"""
    
    def test_spawn_at_interval(self):
        """Test powerup spawns at correct intervals"""
        assert should_spawn_powerup(100, 100) == True
        assert should_spawn_powerup(500, 100) == True
        assert should_spawn_powerup(300, 50) == True
    
    def test_no_spawn_between_intervals(self):
        """Test powerup doesn't spawn between intervals"""
        assert should_spawn_powerup(150, 100) == False
        assert should_spawn_powerup(550, 100) == False
    
    def test_spawn_at_zero(self):
        """Test behavior at score 0"""
        assert should_spawn_powerup(0, 100) == True


class TestGetRank:
    """Tests for get_rank function"""
    
    def test_beginner_rank(self):
        """Test beginner rank"""
        assert get_rank(0) == "Beginner"
        assert get_rank(50) == "Beginner"
        assert get_rank(99) == "Beginner"
    
    def test_intermediate_rank(self):
        """Test intermediate rank"""
        assert get_rank(100) == "Intermediate"
        assert get_rank(300) == "Intermediate"
        assert get_rank(499) == "Intermediate"
    
    def test_advanced_rank(self):
        """Test advanced rank"""
        assert get_rank(500) == "Advanced"
        assert get_rank(750) == "Advanced"
        assert get_rank(999) == "Advanced"
    
    def test_expert_rank(self):
        """Test expert rank"""
        assert get_rank(1000) == "Expert"
        assert get_rank(1500) == "Expert"
        assert get_rank(1999) == "Expert"
    
    def test_master_rank(self):
        """Test master rank"""
        assert get_rank(2000) == "Master"
        assert get_rank(5000) == "Master"


class TestCalculateBonus:
    """Tests for calculate_bonus function"""
    
    def test_no_combo_no_powerup(self):
        """Test base score with no bonuses"""
        assert calculate_bonus(100, 0, False) == 100.0
    
    def test_with_combo_no_powerup(self):
        """Test score with combo multiplier only"""
        result = calculate_bonus(100, 2, False)
        assert result == 120.0  # 100 * 1.2
    
    def test_no_combo_with_powerup(self):
        """Test score with powerup only"""
        result = calculate_bonus(100, 0, True)
        assert result == 150.0  # 100 * 1.5
    
    def test_combo_and_powerup(self):
        """Test score with both combo and powerup"""
        result = calculate_bonus(100, 2, True)
        assert result == 180.0  # 100 * 1.2 * 1.5
    
    def test_large_combo(self):
        """Test with large combo count"""
        result = calculate_bonus(100, 5, False)
        assert result == 150.0  # 100 * 1.5


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
