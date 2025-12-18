"""Tests for Practice Problem 2: Enemy List Management"""
import pytest
import math
from practice_problem_2_starter import *


def test_create_enemy():
    enemy = create_enemy("Goblin", 100, 50, 75)
    assert enemy['name'] == "Goblin"
    assert enemy['health'] == 100
    assert enemy['x'] == 50
    assert enemy['y'] == 75


def test_add_enemy():
    enemies = []
    enemy = create_enemy("Orc", 150, 100, 100)
    add_enemy(enemies, enemy)
    assert len(enemies) == 1
    assert enemies[0]['name'] == "Orc"


def test_remove_dead_enemies():
    enemies = [
        {'health': 10}, {'health': 0}, {'health': -5}, {'health': 50}
    ]
    count = remove_dead_enemies(enemies)
    assert count == 2
    assert len(enemies) == 2


def test_find_enemy_by_name():
    enemies = [
        {'name': "Goblin"}, {'name': "Orc"}, {'name': "Troll"}
    ]
    result = find_enemy_by_name(enemies, "Orc")
    assert result is not None
    assert result['name'] == "Orc"
    assert find_enemy_by_name(enemies, "Dragon") is None


def test_get_closest_enemy():
    enemies = [
        {'x': 100, 'y': 100},
        {'x': 200, 'y': 200},
        {'x': 50, 'y': 50}
    ]
    closest = get_closest_enemy(enemies, 45, 45)
    assert closest['x'] == 50
    assert closest['y'] == 50


def test_damage_all_enemies():
    enemies = [{'health': 100}, {'health': 50}, {'health': 75}]
    damage_all_enemies(enemies, 25)
    assert enemies[0]['health'] == 75
    assert enemies[1]['health'] == 25
    assert enemies[2]['health'] == 50


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
