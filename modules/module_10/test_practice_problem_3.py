"""Tests for Practice Problem 3: Ethical Game Design"""
import pytest
from practice_problem_3_starter import *


def test_check_playtime_limit():
    assert check_playtime_limit(60) == True
    assert check_playtime_limit(150) == False


def test_calculate_fair_matchmaking_score():
    stats = {'wins': 10, 'losses': 5, 'level': 20}
    score = calculate_fair_matchmaking_score(stats)
    assert isinstance(score, (int, float))


def test_detect_toxic_language():
    assert detect_toxic_language("you are terrible") == True
    assert detect_toxic_language("good game friend") == False


def test_suggest_break():
    assert suggest_break(30) == False
    assert suggest_break(90) == True


def test_validate_microtransaction():
    assert validate_microtransaction(5, 18) == True
    assert validate_microtransaction(100, 12) == False


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
