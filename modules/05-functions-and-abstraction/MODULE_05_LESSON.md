# Module 5: Functions and Abstraction

## Learning Objectives
- Create and use functions to organize game code
- Apply parameters and return values for flexible function design
- Understand scope and how functions encapsulate logic
- Recognize functions as the primary abstraction mechanism in programming

## AP CSP Alignment

**Big Idea:** Algorithms and Programming (AAP)

**Specific Standards:**
- AAP-3.A: Call and return values from procedures
- AAP-3.B: Explain how the use of procedural abstraction manages complexity
- AAP-2.A: Express an algorithm that uses sequencing without using a programming language
- AAP-2.B: Represent a step-by-step algorithmic process using sequential code statements

**Computational Thinking Practices:**
- 3.B: Use abstraction to manage complexity
- 3.C: Explain how abstraction manages complexity

## Concept: Functions in Game Development

### What are Functions?

Functions are named blocks of code that perform specific tasks. They are the fundamental abstraction mechanism in programming, allowing us to break complex problems into manageable pieces.

### Key Concepts:

1. **Defining Functions**
```python
def greet_player():
    """Simple function with no parameters"""
    print("Welcome to the game!")

def calculate_damage(base_damage, armor):
    """Function with parameters"""
    actual_damage = base_damage - (armor * 0.1)
    return max(0, actual_damage)
```

2. **Parameters and Arguments**
```python
def spawn_enemy(x, y, enemy_type):
    """Function with multiple parameters"""
    enemy = {
        'x': x,
        'y': y,
        'type': enemy_type,
        'health': 100
    }
    return enemy

# Calling with arguments
new_enemy = spawn_enemy(100, 200, "goblin")
```

3. **Return Values**
```python
def check_collision(obj1, obj2):
    """Returns True if objects collide"""
    distance = ((obj1['x'] - obj2['x'])**2 + 
                (obj1['y'] - obj2['y'])**2)**0.5
    return distance < obj1['size'] + obj2['size']

if check_collision(player, enemy):
    handle_collision()
```

4. **Default Parameters**
```python
def create_particle(x, y, color="white", speed=5):
    """Function with default parameter values"""
    return {'x': x, 'y': y, 'color': color, 'speed': speed}

# Can call with or without optional parameters
particle1 = create_particle(100, 200)
particle2 = create_particle(150, 250, "red", 10)
```

### Functions as Abstraction

Functions are the ultimate abstraction tool in programming:
- **Hide complexity**: Implementation details are hidden inside functions
- **Reusability**: Write once, use many times
- **Modularity**: Break large problems into smaller pieces
- **Maintainability**: Changes in one place affect all uses
- **Readability**: Well-named functions document what code does

## Mini-Lesson: Creating a Game Utility Library

### Example: Helper Functions

```python
# game_utils.py
import random
import math

WIDTH = 800
HEIGHT = 600

def distance(x1, y1, x2, y2):
    """Calculate distance between two points"""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def circle_collision(obj1, obj2):
    """Check collision between two circular objects"""
    dist = distance(obj1['x'], obj1['y'], obj2['x'], obj2['y'])
    return dist < obj1['radius'] + obj2['radius']

def clamp(value, min_val, max_val):
    """Constrain value between min and max"""
    return max(min_val, min(max_val, value))

def wrap_position(x, y, width=WIDTH, height=HEIGHT):
    """Wrap coordinates around screen edges"""
    x = x % width
    y = y % height
    return x, y

def random_position(margin=50):
    """Generate random position with margin from edges"""
    x = random.randint(margin, WIDTH - margin)
    y = random.randint(margin, HEIGHT - margin)
    return x, y

def lerp(start, end, t):
    """Linear interpolation between start and end"""
    return start + (end - start) * t

def create_explosion_particles(x, y, count=10):
    """Generate particle data for explosion effect"""
    particles = []
    for i in range(count):
        angle = (i / count) * 2 * math.pi
        speed = random.uniform(2, 5)
        particle = {
            'x': x,
            'y': y,
            'vx': math.cos(angle) * speed,
            'vy': math.sin(angle) * speed,
            'life': random.randint(20, 40),
            'color': random.choice(["red", "orange", "yellow"])
        }
        particles.append(particle)
    return particles

# Example usage in game
player = {'x': 400, 'y': 300, 'radius': 20}
enemy = {'x': 450, 'y': 350, 'radius': 25}

if circle_collision(player, enemy):
    print("Collision detected!")
    explosion = create_explosion_particles(enemy['x'], enemy['y'])
```

## Practice Problems

### Problem 1: Health and Damage System (Write All Code)

**Task:** Create a comprehensive health system using functions.

**Requirements:**
1. Function `create_entity(name, max_health, armor)` - Creates entity dict
2. Function `take_damage(entity, damage)` - Applies damage with armor calculation
3. Function `heal(entity, amount)` - Heals entity (not above max)
4. Function `is_alive(entity)` - Returns True if health > 0
5. Function `get_health_percent(entity)` - Returns health as percentage
6. Test your functions with player and enemy entities

**Expected Functions:**
```python
def create_entity(name, max_health, armor):
    pass

def take_damage(entity, damage):
    pass

def heal(entity, amount):
    pass

def is_alive(entity):
    pass

def get_health_percent(entity):
    pass

# Test code
player = create_entity("Hero", 100, 10)
enemy = create_entity("Goblin", 50, 5)
```

---

### Problem 2: Debug the Movement System (Debug and Fix)

**Task:** This movement system has bugs. Find and fix them.

```python
# Buggy movement system
import math

WIDTH = 800
HEIGHT = 600

def move_toward(obj, target_x, target_y, speed):
    """Move object toward target at given speed"""
    dx = target_x - obj['x']
    dy = target_y - obj['y']
    distance = math.sqrt(dx**2 + dy**2)  # Bug 1: Not checking for zero distance
    
    # Normalize and apply speed
    obj['x'] += (dx / distance) * speed
    obj['y'] += (dy / distance) * speed

def bounce_off_walls(obj, width, height):
    """Bounce object off screen edges"""
    # Bug 2: Wrong comparison operators
    if obj['x'] < 0 and obj['x'] > width:
        obj['vx'] *= -1
    if obj['y'] < 0 and obj['y'] > height:
        obj['vy'] *= -1  # Bug 3: Doesn't update position

def apply_friction(obj, friction_factor):
    """Apply friction to object velocity"""
    obj['vx'] = obj['vx'] * friction_factor
    obj['vy'] = obj['vy'] * friction_factor
    # Bug 4: No check for very small velocities (should stop)

def update_physics(obj):
    """Update object position based on velocity"""
    obj['x'] += obj['vx']
    obj['y'] += obj['vy']
    apply_friction(obj, 0.98)
    bounce_off_walls(obj, WIDTH, HEIGHT)  # Bug 5: Missing return statement if needed
```

---

### Problem 3: Extend the Scoring System (Add to Existing Program)

**Task:** Extend this scoring system with new functions.

```python
# Basic scoring system
score = 0
combo = 0
combo_timer = 0

def add_points(points):
    """Add points to score"""
    global score
    score += points

def get_score():
    """Return current score"""
    return score

def reset_score():
    """Reset score to zero"""
    global score
    score = 0
```

**Your Tasks:**
1. Add `add_combo_points(base_points)` - Multiplies points by combo value
2. Add `increase_combo()` - Increases combo counter
3. Add `reset_combo()` - Resets combo to 0
4. Add `update_combo_timer()` - Decreases timer, resets combo if reaches 0
5. Add `get_score_grade()` - Returns letter grade (A, B, C, D, F) based on score
6. Add `calculate_stars(score)` - Returns 1-3 stars based on performance

---

## Project Task: Create a Modular Platformer Movement System

### Project Description

Build a character movement system using well-organized functions.

### Requirements

1. **Core Movement Functions:**
   - `move_player(direction, speed)` - Move in cardinal directions
   - `jump(player)` - Apply jump force
   - `apply_gravity(player)` - Apply gravity to player
   - `check_ground_collision(player, platforms)` - Check if on ground
   - `clamp_to_screen(player)` - Keep player on screen

2. **Helper Functions:**
   - `create_player(x, y)` - Initialize player dict
   - `create_platform(x, y, width, height)` - Create platform dict
   - `get_player_rect(player)` - Return Rect for player
   - `get_platform_rect(platform)` - Return Rect for platform

3. **Advanced Functions:**
   - `handle_platform_collision(player, platform)` - Resolve collision
   - `update_player_state(player)` - Update jumping, falling states
   - `draw_player(player)` - Render player with state-based appearance

4. **Game Loop Integration:**
   - Clean draw() function using your drawing functions
   - Clean update() function using your game logic functions
   - Proper separation of concerns

### Starter Template

```python
# platformer_movement.py

WIDTH = 800
HEIGHT = 600

# Game state
player = None
platforms = []

def create_player(x, y):
    pass

def move_player(direction, speed):
    pass

def jump(player):
    pass

def apply_gravity(player):
    pass

def draw():
    pass

def update():
    pass
```

### Assessment Criteria

- **Function Design (40%)**: Well-designed, single-purpose functions
- **Abstraction (30%)**: Effective use of functions to hide complexity
- **Game Mechanics (20%)**: Working movement and collision system
- **Code Quality (10%)**: Clean, documented code

### Extension Ideas

- Double jump mechanic
- Wall sliding and wall jumps
- Variable jump height
- Dashing ability
- Moving platforms

---

## Key Takeaways

1. **Functions organize code** - Break complexity into manageable pieces
2. **Abstraction hides details** - Function names describe what, body describes how
3. **Parameters make functions flexible** - Same function, different inputs
4. **Return values pass data** - Functions produce results
5. **Reusability** - Write once, use many times
6. **Single Responsibility** - Each function should do one thing well

## Additional Resources

- Python Functions Documentation
- Function Design Best Practices
- AP CSP Reference Sheet: Procedures and Functions

## Next Module

In Module 6, we'll explore **Dictionaries and Game Data Structures**, learning how to organize complex game data effectively.
