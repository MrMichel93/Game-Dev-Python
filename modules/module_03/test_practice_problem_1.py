"""
Tests for Practice Problem 1: Loop Patterns
Run with: pytest test_practice_problem_1.py
"""

import pytest
from practice_problem_1_starter import (
    sum_range,
    count_multiples,
    create_sequence,
    find_first_divisible,
    generate_grid_positions,
    repeat_pattern
)


class TestSumRange:
    """Tests for sum_range function"""
    
    def test_simple_range(self):
        """Test sum of simple range"""
        assert sum_range(1, 5) == 15  # 1+2+3+4+5
    
    def test_larger_range(self):
        """Test sum of larger range"""
        assert sum_range(10, 15) == 75  # 10+11+12+13+14+15
    
    def test_single_number(self):
        """Test range with single number"""
        assert sum_range(5, 5) == 5
    
    def test_starting_from_zero(self):
        """Test range starting from 0"""
        assert sum_range(0, 3) == 6  # 0+1+2+3


class TestCountMultiples:
    """Tests for count_multiples function"""
    
    def test_multiples_of_3(self):
        """Test counting multiples of 3"""
        assert count_multiples(3, 10) == 3  # 3, 6, 9
    
    def test_multiples_of_5(self):
        """Test counting multiples of 5"""
        assert count_multiples(5, 25) == 5  # 5, 10, 15, 20, 25
    
    def test_multiples_of_1(self):
        """Test counting multiples of 1"""
        assert count_multiples(1, 10) == 10  # All numbers
    
    def test_no_multiples(self):
        """Test when no complete multiple exists"""
        assert count_multiples(20, 15) == 0


class TestCreateSequence:
    """Tests for create_sequence function"""
    
    def test_simple_sequence(self):
        """Test simple sequence"""
        assert create_sequence(5, 4, 2) == [5, 7, 9, 11]
    
    def test_sequence_with_larger_step(self):
        """Test sequence with larger step"""
        assert create_sequence(10, 3, 5) == [10, 15, 20]
    
    def test_sequence_with_step_1(self):
        """Test sequence with step of 1"""
        assert create_sequence(1, 5, 1) == [1, 2, 3, 4, 5]
    
    def test_single_element(self):
        """Test sequence with one element"""
        assert create_sequence(100, 1, 10) == [100]


class TestFindFirstDivisible:
    """Tests for find_first_divisible function"""
    
    def test_find_divisible_by_3(self):
        """Test finding first number divisible by 3"""
        assert find_first_divisible(10, 3) == 12
    
    def test_find_divisible_by_7(self):
        """Test finding first number divisible by 7"""
        assert find_first_divisible(20, 7) == 21
    
    def test_start_is_divisible(self):
        """Test when start is already divisible"""
        assert find_first_divisible(15, 5) == 15
    
    def test_find_divisible_by_1(self):
        """Test divisible by 1 (always returns start)"""
        assert find_first_divisible(42, 1) == 42


class TestGenerateGridPositions:
    """Tests for generate_grid_positions function"""
    
    def test_2x2_grid(self):
        """Test 2x2 grid generation"""
        result = generate_grid_positions(2, 2, 50)
        expected = [(0, 0), (50, 0), (0, 50), (50, 50)]
        assert result == expected
    
    def test_1x3_grid(self):
        """Test 1x3 grid generation"""
        result = generate_grid_positions(1, 3, 100)
        expected = [(0, 0), (100, 0), (200, 0)]
        assert result == expected
    
    def test_3x1_grid(self):
        """Test 3x1 grid generation"""
        result = generate_grid_positions(3, 1, 25)
        expected = [(0, 0), (0, 25), (0, 50)]
        assert result == expected
    
    def test_grid_size(self):
        """Test that grid has correct number of positions"""
        result = generate_grid_positions(4, 5, 10)
        assert len(result) == 20  # 4 * 5


class TestRepeatPattern:
    """Tests for repeat_pattern function"""
    
    def test_repeat_numbers(self):
        """Test repeating number pattern"""
        assert repeat_pattern([1, 2, 3], 2) == [1, 2, 3, 1, 2, 3]
    
    def test_repeat_strings(self):
        """Test repeating string pattern"""
        assert repeat_pattern(['a', 'b'], 3) == ['a', 'b', 'a', 'b', 'a', 'b']
    
    def test_single_repeat(self):
        """Test repeating once"""
        assert repeat_pattern([5, 10], 1) == [5, 10]
    
    def test_no_repeat(self):
        """Test not repeating (0 times)"""
        assert repeat_pattern([1, 2], 0) == []


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
