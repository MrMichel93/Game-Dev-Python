"""Tests for Practice Problem 1: Data Privacy and Validation"""
import pytest
from practice_problem_1_starter import *


def test_validate_username():
    assert validate_username("player123") == True
    assert validate_username("ab") == False  # Too short
    assert validate_username("a" * 25) == False  # Too long


def test_sanitize_input():
    result = sanitize_input("Hello <script>World</script>")
    assert "<" not in result
    assert ">" not in result


def test_hash_password():
    hash1 = hash_password("password123")
    hash2 = hash_password("password123")
    assert hash1 == hash2  # Same input, same hash


def test_validate_age():
    assert validate_age(18) == True
    assert validate_age(10) == False
    assert validate_age(150) == False


def test_mask_email():
    masked = mask_email("john@example.com")
    assert masked.startswith("jo")
    assert "@example.com" in masked


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
