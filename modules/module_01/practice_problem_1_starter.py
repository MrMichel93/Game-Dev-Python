"""
Practice Problem 1: Player Stats Manager
Task: Create functions to manage player statistics in a game.

Instructions:
Complete the functions below to manage a player's game statistics.
Each function should work independently and return the correct value.
Do NOT modify the function signatures or add/remove parameters.
"""

# Complete these functions

def create_player_stats(name, health, attack, defense):
    """
    Create a player stats dictionary with the given values.
    
    Args:
        name (str): Player's name
        health (int): Player's health points
        attack (int): Player's attack power
        defense (int): Player's defense power
    
    Returns:
        dict: A dictionary containing all player stats
    
    Example:
        >>> create_player_stats("Hero", 100, 20, 15)
        {'name': 'Hero', 'health': 100, 'attack': 20, 'defense': 15}
    """
    # TODO: Create and return a dictionary with the player stats
    pass


def calculate_damage(attacker_attack, defender_defense):
    """
    Calculate damage dealt based on attacker's attack and defender's defense.
    Formula: damage = max(1, attack - defense)
    
    Args:
        attacker_attack (int): Attacker's attack power
        defender_defense (int): Defender's defense power
    
    Returns:
        int: The damage dealt (minimum 1)
    
    Example:
        >>> calculate_damage(20, 15)
        5
        >>> calculate_damage(10, 15)
        1
    """
    # TODO: Calculate and return the damage
    pass


def apply_damage(player_health, damage):
    """
    Apply damage to player health, ensuring it doesn't go below 0.
    
    Args:
        player_health (int): Current player health
        damage (int): Damage to apply
    
    Returns:
        int: New health value (minimum 0)
    
    Example:
        >>> apply_damage(100, 30)
        70
        >>> apply_damage(20, 50)
        0
    """
    # TODO: Calculate and return the new health
    pass


def is_alive(health):
    """
    Check if a player is still alive.
    
    Args:
        health (int): Player's current health
    
    Returns:
        bool: True if health > 0, False otherwise
    
    Example:
        >>> is_alive(50)
        True
        >>> is_alive(0)
        False
    """
    # TODO: Return whether the player is alive
    pass


def level_up_stats(attack, defense, level_bonus):
    """
    Increase attack and defense by the level bonus amount.
    
    Args:
        attack (int): Current attack power
        defense (int): Current defense power
        level_bonus (int): Amount to increase each stat
    
    Returns:
        tuple: (new_attack, new_defense)
    
    Example:
        >>> level_up_stats(20, 15, 5)
        (25, 20)
    """
    # TODO: Calculate and return the new stats as a tuple
    pass
