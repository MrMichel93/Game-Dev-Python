# Module 4: Lists and Sprite Management

## Learning Objectives
- Use lists to manage collections of game objects
- Apply list methods to add, remove, and modify game elements
- Understand indexing and slicing for accessing list elements
- Recognize lists as abstractions for managing multiple related items

## AP CSP Alignment

**Big Idea:** Data (DAT)

**Specific Standards:**
- DAT-2.A: Represent a list or string using a variable
- DAT-2.B: Determine the result of list operations
- DAT-2.C: Access elements in a list
- AAP-1.D: Represent a list or string using a variable (in programming context)

**Computational Thinking Practices:**
- 3.C: Explain how abstraction manages complexity
- 4.B: Determine the result of code segments

## Concept: Lists in Game Development

### What are Lists?

Lists are ordered collections that can store multiple values. In game development, lists are essential for managing sprites, enemies, bullets, items, and any collection of similar objects.

### Key Concepts:

1. **Creating Lists**
```python
# Empty list
enemies = []

# List with initial values
lives_icons = ["❤", "❤", "❤"]

# List of different types
game_data = [100, "Player1", True, 3.5]
```

2. **Accessing Elements**
```python
# Indexing (0-based)
first_enemy = enemies[0]
last_enemy = enemies[-1]

# Slicing
first_three = enemies[0:3]
last_two = enemies[-2:]
```

3. **Modifying Lists**
```python
# Adding elements
enemies.append(new_enemy)
bullets.extend([bullet1, bullet2])
powerups.insert(0, powerup)

# Removing elements
enemies.remove(enemy)
bullet = bullets.pop()
del coins[0]

# Modifying elements
enemies[2]['health'] -= 10
```

4. **List Operations**
```python
# Length
num_enemies = len(enemies)

# Check membership
if player in active_players:
    update_player(player)

# Concatenation
all_objects = enemies + allies + neutrals
```

### Lists as Abstraction

Lists abstract the concept of collections. Instead of managing individual variables (`enemy1`, `enemy2`, `enemy3`...), we manage a single list. This abstraction:
- Allows dynamic sizing (add/remove items)
- Enables batch operations (loop through all)
- Simplifies game logic
- Makes code more maintainable

## Mini-Lesson: Managing a Collection of Enemies

### Example: Enemy Wave System

```python
# enemy_wave.py
import random

WIDTH = 800
HEIGHT = 600

enemies = []
player_x = WIDTH // 2
player_y = HEIGHT - 50
score = 0

def draw():
    screen.fill((0, 0, 40))
    
    # Draw player
    screen.draw.filled_circle((player_x, player_y), 15, "blue")
    
    # Draw all enemies using list
    for enemy in enemies:
        screen.draw.filled_circle(
            (enemy['x'], enemy['y']),
            enemy['size'],
            enemy['color']
        )
    
    # Display info
    screen.draw.text(f"Enemies: {len(enemies)}", (10, 10), color="white")
    screen.draw.text(f"Score: {score}", (10, 35), color="white")

def update():
    global score
    
    # Spawn new enemies randomly
    if random.random() < 0.02:  # 2% chance per frame
        enemy = {
            'x': random.randint(20, WIDTH - 20),
            'y': -20,  # Start above screen
            'speed': random.uniform(1, 3),
            'size': random.randint(10, 20),
            'color': "red"
        }
        enemies.append(enemy)
    
    # Update all enemies
    for enemy in enemies:
        enemy['y'] += enemy['speed']
    
    # Remove off-screen enemies (using list comprehension)
    enemies_before = len(enemies)
    enemies[:] = [e for e in enemies if e['y'] < HEIGHT + 50]
    score += enemies_before - len(enemies)
```

## Practice Problems

### Problem 1: Inventory Management System (Write All Code)

**Task:** Create an inventory system using lists.

**Requirements:**
1. Create an inventory list that can hold up to 10 items
2. Items have: name, quantity, and icon/color
3. Display inventory in a grid (2 rows of 5)
4. Add items to inventory (stack if same item)
5. Remove items from inventory
6. Show "Inventory Full" message when at capacity

**Starter Code Structure:**
```python
WIDTH = 800
HEIGHT = 600

inventory = []
MAX_INVENTORY = 10

def draw():
    # Draw inventory grid
    pass

def add_item(item_name):
    # Add item to inventory
    pass

def remove_item(index):
    # Remove item from inventory
    pass
```

---

### Problem 2: Debug the Bullet System (Debug and Fix)

**Task:** This bullet management system has bugs. Find and fix them.

```python
# Buggy bullet system
WIDTH = 800
HEIGHT = 600

bullets = []
player_x = WIDTH // 2

def draw():
    screen.fill((0, 0, 50))
    
    # Draw player
    screen.draw.filled_circle((player_x, HEIGHT - 30), 20, "blue")
    
    # Draw bullets
    for bullet in bullets:
        screen.draw.filled_circle(
            (bullet['x'], bullet['y']),
            5,
            "yellow"
        )
    
    screen.draw.text(f"Bullets: {len(bullets)}", (10, 10), color="white")

def update():
    # Update bullets - Bug 1: Modifying list while iterating
    for bullet in bullets:
        bullet['y'] -= 5
        
        # Remove if off screen
        if bullet['y'] < 0:
            bullets.remove(bullet)
    
    # Fire bullet periodically
    if len(bullets) < 5:  # Bug 2: Should use frame counter, not constant checking
        bullet = {
            'x': player_x,
            'y': HEIGHT - 50
        }
        bullets.append(bullet)  # Bug 3: Creates too many bullets

def on_key_down(key):
    # Bug 4: No way for player to actually fire bullets
    pass
```

**Instructions:**
1. Fix the list modification bug
2. Add proper bullet firing control
3. Add bullet limit system
4. Implement player movement and firing

---

### Problem 3: Extend the Powerup System (Add to Existing Program)

**Task:** Extend this powerup system with new features.

```python
# Basic powerup system
import random

WIDTH = 800
HEIGHT = 600

powerups = []
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 5
score = 0

POWERUP_TYPES = ["speed", "shield", "points"]

def draw():
    screen.fill((20, 20, 20))
    
    # Draw player
    screen.draw.filled_circle((player_x, player_y), 20, "blue")
    
    # Draw powerups
    for powerup in powerups:
        color = get_powerup_color(powerup['type'])
        screen.draw.filled_rect(
            Rect(powerup['x'], powerup['y'], 30, 30),
            color
        )
    
    screen.draw.text(f"Score: {score}", (10, 10), color="white")

def get_powerup_color(powerup_type):
    if powerup_type == "speed":
        return "cyan"
    elif powerup_type == "shield":
        return "yellow"
    elif powerup_type == "points":
        return "green"

def update():
    global score
    
    # Spawn powerups
    if random.random() < 0.01:
        powerup = {
            'x': random.randint(0, WIDTH - 30),
            'y': 0,
            'type': random.choice(POWERUP_TYPES),
            'speed': 2
        }
        powerups.append(powerup)
    
    # Update powerups
    for powerup in powerups:
        powerup['y'] += powerup['speed']
    
    # Remove off-screen powerups
    powerups[:] = [p for p in powerups if p['y'] < HEIGHT]
    
    # Check collisions (simplified)
    # TODO: Implement collision detection
```

**Your Tasks:**
1. Implement collision detection between player and powerups
2. Add effects for each powerup type (store in a separate list)
3. Add duration timers for active powerups
4. Display active powerups on screen
5. Add visual feedback when collecting powerups

**Bonus Challenge:** Add powerup stacking and combo effects.

---

## Project Task: Create a Space Shooter Enemy Wave System

### Project Description

Build a space shooter with multiple enemy types managed using lists.

### Requirements

1. **Multiple Enemy Types:**
   - At least 3 different enemy types (different behaviors, colors, points)
   - Store enemies in a list
   - Each enemy is a dictionary with properties

2. **Wave System:**
   - Spawn enemies in waves
   - Track wave number
   - Increase difficulty with each wave
   - Clear indication between waves

3. **Player Interaction:**
   - Player can move
   - Player can shoot (bullets in a list)
   - Collision detection between bullets and enemies
   - Score based on enemy type

4. **List Operations:**
   - Add enemies to list when spawning
   - Remove enemies when destroyed
   - Remove bullets when off-screen or hit
   - Use list comprehensions for cleanup

5. **Visual Design:**
   - Different colors/shapes for enemy types
   - Score and wave display
   - Visual effects for destruction

### Starter Template

```python
# space_shooter.py
import random

WIDTH = 800
HEIGHT = 600

# Game lists
enemies = []
bullets = []
particles = []

# Game state
wave_number = 1
score = 0
player_x = WIDTH // 2

def spawn_wave(wave_num):
    # Spawn enemies based on wave number
    pass

def draw():
    # Draw everything
    pass

def update():
    # Update all game objects
    pass
```

### Assessment Criteria

- **List Management (40%)**: Effective use of lists for game objects
- **Game Mechanics (30%)**: Working collision, spawning, and wave systems
- **Code Quality (15%)**: Clean, organized code with comments
- **Visual Polish (15%)**: Good visual feedback and design

### Extension Ideas

- Boss enemies at certain waves
- Multiple bullet types
- Player health system
- Powerup drops from enemies
- High score persistence

---

## Key Takeaways

1. **Lists manage collections** - Essential for multiple game objects
2. **List methods** - append, remove, pop, insert for modifications
3. **List comprehensions** - Efficient filtering and transformation
4. **Iteration patterns** - Loop through lists to process all items
5. **Abstraction** - Lists simplify managing many similar objects

## Additional Resources

- Python Lists Documentation
- List Comprehensions Guide
- AP CSP Reference Sheet: Lists

## Next Module

In Module 5, we'll explore **Functions and Abstraction**, learning how to organize code into reusable, manageable pieces.
