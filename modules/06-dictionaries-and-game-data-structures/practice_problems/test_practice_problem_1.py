"""Tests for Practice Problem 1: Dictionary Operations"""
import pytest
from practice_problem_1_starter import *


def test_create_player():
    player = create_player("Hero", 100, 200, 100)
    assert player['name'] == "Hero"
    assert player['x'] == 100


def test_get_player_info():
    player = {'name': "Hero", 'health': 100}
    assert get_player_info(player, 'name') == "Hero"
    assert get_player_info(player, 'mana', 0) == 0


def test_update_player_position():
    player = {'x': 0, 'y': 0}
    update_player_position(player, 50, 75)
    assert player['x'] == 50
    assert player['y'] == 75


def test_add_item_to_player():
    player = {}
    add_item_to_player(player, "sword")
    assert 'inventory' in player
    assert "sword" in player['inventory']


def test_calculate_player_stats():
    player = {'attack': 10, 'defense': 5}
    stats = calculate_player_stats(player)
    assert isinstance(stats, dict)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
