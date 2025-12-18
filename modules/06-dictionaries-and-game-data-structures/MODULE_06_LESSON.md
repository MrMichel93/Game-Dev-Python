# Module 6: Dictionaries and Game Data Structures

## Learning Objectives
- Use dictionaries to organize complex game data
- Apply key-value pairs to represent game entities and states
- Compare dictionaries with lists to choose appropriate data structures
- Understand how dictionaries abstract data organization

## AP CSP Alignment

**Big Idea:** Data (DAT)

**Specific Standards:**
- DAT-2.A: Represent collections of related data using multiple variables
- DAT-2.B: Determine the result of operations on collections
- DAT-2.D: Extract information from data
- AAP-1.D: Evaluate expressions that manipulate data structures

**Computational Thinking Practices:**
- 3.C: Explain how abstraction manages complexity in data representation
- 4.B: Determine the result of code segments

## Concept: Dictionaries in Game Development

### What are Dictionaries?

Dictionaries store data as key-value pairs, allowing you to organize related information under meaningful names. They're perfect for representing game entities, configurations, and states.

### Key Concepts:

1. **Creating Dictionaries**
```python
# Empty dictionary
player = {}

# Dictionary with initial values
player = {
    'name': 'Hero',
    'x': 400,
    'y': 300,
    'health': 100,
    'armor': 10,
    'inventory': []
}
```

2. **Accessing and Modifying Values**
```python
# Access values
player_health = player['health']
player_x = player.get('x', 0)  # With default value

# Modify values
player['health'] -= 10
player['x'] += 5

# Add new keys
player['mana'] = 50
```

3. **Dictionary Methods**
```python
# Get all keys
stats = player.keys()

# Get all values
values = player.values()

# Get key-value pairs
items = player.items()

# Check if key exists
if 'mana' in player:
    use_mana()
```

4. **Nested Dictionaries**
```python
game_state = {
    'player': {
        'position': {'x': 400, 'y': 300},
        'stats': {'health': 100, 'mana': 50},
        'inventory': ['sword', 'shield']
    },
    'level': {
        'number': 1,
        'enemies_remaining': 5,
        'time_limit': 300
    }
}

# Accessing nested values
player_x = game_state['player']['position']['x']
```

### Dictionaries as Abstraction

Dictionaries abstract the concept of "objects with properties":
- **Named access**: Use meaningful names instead of numeric indices
- **Flexible structure**: Add/remove properties as needed
- **Self-documenting**: Keys describe what each value represents
- **Grouping**: Keep related data together

## Mini-Lesson: Building a Game Entity System

### Example: Entity Management

```python
# entity_system.py
import random

WIDTH = 800
HEIGHT = 600

def create_player(name, x, y):
    """Create a player entity"""
    return {
        'type': 'player',
        'name': name,
        'x': x,
        'y': y,
        'width': 40,
        'height': 40,
        'health': 100,
        'max_health': 100,
        'speed': 5,
        'color': 'blue',
        'inventory': [],
        'stats': {
            'strength': 10,
            'defense': 5,
            'agility': 8
        }
    }

def create_enemy(enemy_type, x, y):
    """Create an enemy based on type"""
    enemy_types = {
        'goblin': {
            'health': 30,
            'speed': 2,
            'damage': 5,
            'color': 'green',
            'size': 25,
            'points': 10
        },
        'orc': {
            'health': 60,
            'speed': 1,
            'damage': 15,
            'color': 'red',
            'size': 35,
            'points': 25
        },
        'dragon': {
            'health': 200,
            'speed': 3,
            'damage': 30,
            'color': 'purple',
            'size': 50,
            'points': 100
        }
    }
    
    template = enemy_types.get(enemy_type, enemy_types['goblin'])
    
    return {
        'type': 'enemy',
        'enemy_type': enemy_type,
        'x': x,
        'y': y,
        'health': template['health'],
        'max_health': template['health'],
        'speed': template['speed'],
        'damage': template['damage'],
        'color': template['color'],
        'size': template['size'],
        'points': template['points'],
        'state': 'patrol'  # patrol, chase, attack
    }

def create_item(item_type, x, y):
    """Create a collectible item"""
    items = {
        'health_potion': {
            'name': 'Health Potion',
            'color': 'red',
            'effect': {'health': 25}
        },
        'coin': {
            'name': 'Gold Coin',
            'color': 'yellow',
            'effect': {'score': 10}
        },
        'power_star': {
            'name': 'Power Star',
            'color': 'gold',
            'effect': {'strength': 5, 'invincible_time': 300}
        }
    }
    
    template = items[item_type]
    
    return {
        'type': 'item',
        'item_type': item_type,
        'x': x,
        'y': y,
        'name': template['name'],
        'color': template['color'],
        'effect': template['effect'],
        'size': 20
    }

# Example usage
player = create_player("Hero", 100, 100)
goblin = create_enemy("goblin", 300, 200)
potion = create_item("health_potion", 400, 150)

print(f"Player: {player['name']} at ({player['x']}, {player['y']})")
print(f"Enemy: {goblin['enemy_type']} with {goblin['health']} HP")
print(f"Item: {potion['name']} provides {potion['effect']}")
```

## Practice Problems

### Problem 1: Game Configuration System (Write All Code)

**Task:** Create a configuration system using dictionaries.

**Requirements:**
1. Create a `config` dictionary with game settings:
   - window_settings: width, height, title, fps
   - player_settings: speed, jump_height, max_health
   - enemy_settings: spawn_rate, max_count
   - difficulty_levels: easy, medium, hard (each with multipliers)
2. Function `get_setting(path)` - Access nested settings (e.g., "player_settings.speed")
3. Function `apply_difficulty(level)` - Modify settings based on difficulty
4. Function `save_config()` - Print config in readable format
5. Function `validate_config()` - Check if all required settings exist

**Expected Structure:**
```python
config = {
    'window_settings': {
        # your settings
    },
    # ... more settings
}

def get_setting(path):
    pass
```

---

### Problem 2: Debug the Inventory System (Debug and Fix)

**Task:** This inventory system has bugs. Fix them.

```python
# Buggy inventory system
player = {
    'name': 'Hero',
    'inventory': [],
    'max_inventory': 10,
    'gold': 0
}

items_database = {
    'sword': {'name': 'Iron Sword', 'damage': 10, 'value': 50},
    'shield': {'name': 'Wooden Shield', 'defense': 5, 'value': 30},
    'potion': {'name': 'Health Potion', 'healing': 25, 'value': 15}
}

def add_to_inventory(item_id):
    """Add item to player inventory"""
    # Bug 1: Doesn't check if inventory is full
    item = items_database[item_id]  # Bug 2: No error handling if item doesn't exist
    player['inventory'].append(item)
    print(f"Added {item['name']} to inventory")

def remove_from_inventory(item_name):
    """Remove item by name"""
    # Bug 3: Removes first item regardless of name
    player['inventory'].pop(0)

def get_inventory_value():
    """Calculate total value of inventory"""
    total = 0
    for item in player['inventory']:
        total += item['value']
    # Bug 4: Doesn't return the value
    print(f"Total value: {total}")

def use_item(item_index):
    """Use an item from inventory"""
    item = player['inventory'][item_index]  # Bug 5: No bounds checking
    
    if 'healing' in item:
        player['health'] += item['healing']  # Bug 6: player dict has no 'health' key
        remove_from_inventory(item['name'])
```

---

### Problem 3: Extend the Quest System (Add to Existing Program)

**Task:** Extend this quest tracking system.

```python
# Basic quest system
active_quests = []

quest_templates = {
    'fetch_quest': {
        'title': 'Gather Resources',
        'description': 'Collect 10 crystals',
        'type': 'collect',
        'target': 'crystal',
        'goal': 10,
        'reward_gold': 50,
        'reward_xp': 100
    }
}

def start_quest(quest_id):
    """Start a new quest"""
    template = quest_templates[quest_id]
    quest = template.copy()
    quest['id'] = quest_id
    quest['progress'] = 0
    quest['completed'] = False
    active_quests.append(quest)
    return quest

def update_quest_progress(quest_id, progress):
    """Update quest progress"""
    for quest in active_quests:
        if quest['id'] == quest_id:
            quest['progress'] += progress
            if quest['progress'] >= quest['goal']:
                quest['completed'] = True
```

**Your Tasks:**
1. Add more quest templates (kill enemies, reach location, time challenge)
2. Add `complete_quest(quest_id)` - Awards rewards and removes quest
3. Add `get_quest_by_id(quest_id)` - Returns quest dict or None
4. Add quest requirements (minimum level, prerequisite quests)
5. Add `display_quest_log()` - Show all active quests with progress
6. Add quest status: not_started, active, completed, failed

---

## Project Task: Create an RPG Character and Stat System

### Project Description

Build a comprehensive character system using dictionaries.

### Requirements

1. **Character Creation:**
   - Function to create character with customizable attributes
   - Stats: strength, agility, intelligence, vitality
   - Derived stats: max_health, max_mana, damage, defense
   - Character class affects starting stats

2. **Inventory System:**
   - Equipment slots: weapon, armor, accessory
   - Consumable items in separate list
   - Item effects modify character stats
   - Weight/capacity system

3. **Progression System:**
   - Experience points and leveling
   - Stat increases on level up
   - Skills/abilities unlock at certain levels
   - Track total playtime and achievements

4. **Status Effects:**
   - Buffs and debuffs (dictionary of active effects)
   - Duration tracking
   - Stack limits for each effect type

5. **Save/Load System:**
   - Function to serialize character to dictionary
   - Function to create character from saved data
   - Display character sheet

### Starter Template

```python
# rpg_character_system.py

def create_character(name, character_class):
    """Create a new character"""
    pass

def equip_item(character, slot, item):
    """Equip an item to character"""
    pass

def gain_experience(character, xp):
    """Add XP and handle level ups"""
    pass

def apply_status_effect(character, effect_name, duration):
    """Apply a status effect"""
    pass

def update_status_effects(character):
    """Update durations of active effects"""
    pass

def calculate_stats(character):
    """Calculate derived stats from base stats and equipment"""
    pass

def save_character(character):
    """Return dictionary representation for saving"""
    pass

def load_character(data):
    """Create character from saved data"""
    pass
```

### Assessment Criteria

- **Dictionary Usage (40%)**: Effective use of dictionaries for data organization
- **System Design (30%)**: Well-thought-out stat and progression systems
- **Functionality (20%)**: All required features working correctly
- **Code Quality (10%)**: Clean, documented code

### Extension Ideas

- Party system (multiple characters)
- Skill trees with dependencies
- Crafting system
- Character comparison tools
- Procedural item generation

---

## Key Takeaways

1. **Dictionaries organize related data** - Perfect for game entities
2. **Key-value pairs** - Named access is more readable than indices
3. **Flexible structure** - Easy to add/modify properties
4. **Nested dictionaries** - Model complex hierarchical data
5. **Abstraction** - Hide data structure complexity behind meaningful names

## Additional Resources

- Python Dictionaries Documentation
- Data Structure Design Patterns
- AP CSP Reference Sheet: Dictionaries and Data Structures

## Next Module

In Module 7, we'll explore **Event Handling and User Input**, learning how to make games interactive and responsive.
