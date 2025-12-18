"""
Tests for Practice Problem 1: Player Stats Manager
Run with: pytest test_practice_problem_1.py
"""

import pytest
from practice_problem_1_starter import (
    create_player_stats,
    calculate_damage,
    apply_damage,
    is_alive,
    level_up_stats
)


class TestCreatePlayerStats:
    """Tests for create_player_stats function"""
    
    def test_basic_stats(self):
        """Test creating basic player stats"""
        result = create_player_stats("Hero", 100, 20, 15)
        assert result == {'name': 'Hero', 'health': 100, 'attack': 20, 'defense': 15}
    
    def test_different_values(self):
        """Test with different stat values"""
        result = create_player_stats("Warrior", 150, 30, 25)
        assert result == {'name': 'Warrior', 'health': 150, 'attack': 30, 'defense': 25}
    
    def test_zero_stats(self):
        """Test with zero values"""
        result = create_player_stats("Newbie", 0, 0, 0)
        assert result == {'name': 'Newbie', 'health': 0, 'attack': 0, 'defense': 0}


class TestCalculateDamage:
    """Tests for calculate_damage function"""
    
    def test_normal_damage(self):
        """Test normal damage calculation"""
        assert calculate_damage(20, 15) == 5
    
    def test_high_attack(self):
        """Test with much higher attack"""
        assert calculate_damage(100, 20) == 80
    
    def test_minimum_damage(self):
        """Test that minimum damage is 1"""
        assert calculate_damage(10, 15) == 1
        assert calculate_damage(5, 20) == 1
    
    def test_equal_stats(self):
        """Test when attack equals defense"""
        assert calculate_damage(15, 15) == 1


class TestApplyDamage:
    """Tests for apply_damage function"""
    
    def test_normal_damage_application(self):
        """Test normal damage application"""
        assert apply_damage(100, 30) == 70
    
    def test_health_not_below_zero(self):
        """Test that health doesn't go below 0"""
        assert apply_damage(20, 50) == 0
        assert apply_damage(10, 100) == 0
    
    def test_zero_damage(self):
        """Test applying zero damage"""
        assert apply_damage(100, 0) == 100
    
    def test_exact_damage(self):
        """Test damage that exactly depletes health"""
        assert apply_damage(50, 50) == 0


class TestIsAlive:
    """Tests for is_alive function"""
    
    def test_alive_with_full_health(self):
        """Test with full health"""
        assert is_alive(100) == True
    
    def test_alive_with_low_health(self):
        """Test with low but positive health"""
        assert is_alive(1) == True
    
    def test_dead_with_zero_health(self):
        """Test with zero health"""
        assert is_alive(0) == False
    
    def test_dead_with_negative_health(self):
        """Test with negative health (edge case)"""
        assert is_alive(-10) == False


class TestLevelUpStats:
    """Tests for level_up_stats function"""
    
    def test_normal_level_up(self):
        """Test normal level up"""
        assert level_up_stats(20, 15, 5) == (25, 20)
    
    def test_large_bonus(self):
        """Test with large level bonus"""
        assert level_up_stats(10, 10, 50) == (60, 60)
    
    def test_zero_bonus(self):
        """Test with zero bonus"""
        assert level_up_stats(20, 15, 0) == (20, 15)
    
    def test_returns_tuple(self):
        """Test that function returns a tuple"""
        result = level_up_stats(20, 15, 5)
        assert isinstance(result, tuple)
        assert len(result) == 2


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
