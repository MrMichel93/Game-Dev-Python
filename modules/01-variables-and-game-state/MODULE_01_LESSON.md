# Module 1: Variables and Game State

## Learning Objectives
- Understand how variables represent game state in a dynamic system
- Apply variables to store and modify player position, score, and game properties
- Recognize variables as abstractions that simplify game data management

## AP CSP Alignment

**Big Idea:** Data (DAT)

**Specific Standards:**
- DAT-1.A: Represent a value with a variable
- DAT-1.B: Determine the value of a variable as a result of an assignment
- AAP-1.A: Represent a value with a variable (in the context of programming)

**Computational Thinking Practices:**
- 4.B: Determine the result of code segments
- 2.B: Implement an algorithm

## Concept: Variables in Game Development

### What are Variables?

Variables are named containers that store data. In game development, variables are essential for tracking the game state—everything from player position to score to game status.

### Key Concepts:

1. **Variable Declaration and Assignment**
```python
# Basic variable assignment
player_x = 100
player_y = 200
score = 0
game_active = True
```

2. **Variable Types in Games**
```python
# Numeric variables (int, float)
health = 100        # integer
speed = 2.5         # float

# String variables
player_name = "Hero"
game_title = "Space Adventure"

# Boolean variables
is_jumping = False
game_over = False
```

3. **Updating Variables**
```python
# Increment score
score = score + 10
# or using shorthand
score += 10

# Update position
player_x = player_x + speed
player_x += speed  # shorthand
```

### Variables as Abstraction

Variables abstract away the complexity of memory management. Instead of thinking about memory addresses, we use meaningful names like `player_x` or `score`. This abstraction allows us to:
- Write more readable code
- Focus on game logic rather than technical details
- Easily modify and maintain our game

## Mini-Lesson: Creating Your First Game Variables

### Example: Simple Game State

```python
# game_state.py
# This program demonstrates basic game variables

# Window dimensions
WIDTH = 800
HEIGHT = 600

# Player state
player_x = 400
player_y = 300
player_speed = 5

# Game state
score = 0
lives = 3
level = 1

def draw():
    screen.fill((0, 0, 0))  # Black background
    screen.draw.text(f"Score: {score}", (10, 10), color="white")
    screen.draw.text(f"Lives: {lives}", (10, 30), color="white")
    screen.draw.text(f"Level: {level}", (10, 50), color="white")
    screen.draw.filled_circle((player_x, player_y), 20, "blue")

def update():
    global player_x
    # Move player right automatically
    player_x += player_speed
    
    # Wrap around screen
    if player_x > WIDTH:
        player_x = 0
```

### Understanding the Code

- **Global Variables:** `WIDTH`, `HEIGHT`, etc. are defined at the module level
- **The `global` keyword:** Used inside functions to modify global variables
- **String Formatting:** `f"Score: {score}"` embeds variable values in strings
- **Type Flexibility:** Python automatically handles variable types

## Practice Problems

### Problem 1: Create a Complete Game State (Write All Code)

**Task:** Write a Pygame Zero program that displays a player character (circle) with the following properties stored in variables:
- Position (x, y coordinates)
- Size (radius)
- Color (as a string or RGB tuple)
- Name (string displayed above the character)

Your program should:
1. Define all necessary variables
2. Display the character at the specified position
3. Show the character's name above it
4. Allow the character to move right by 3 pixels each frame

**Starter Code Structure:**
```python
# Define your variables here

def draw():
    # Your drawing code here
    pass

def update():
    # Your update code here
    pass
```

**Expected Output:** A window showing a colored circle that moves across the screen with a name label above it.

---

### Problem 2: Debug the Score System (Debug and Fix)

**Task:** The following code is supposed to track a player's score and display it, but it has several bugs. Find and fix all the bugs.

```python
# Buggy score system
WIDTH = 800
HEIGHT = 600

# Game variables
score = 0
bonus_points = 50
player_name = Hero  # Bug 1: Missing quotes
high_score = 100

def draw():
    screen.fill((0, 0, 0))
    screen.draw.text(f"Player: {player_name}", (10, 10), color="white")
    screen.draw.text(f"Score: {Score}", (10, 30), color="white")  # Bug 2: Wrong variable name
    screen.draw.text(f"High Score: {high_score}", (10, 50), color="white")

def update():
    # Add bonus points every frame
    score = score + bonus_points  # Bug 3: Missing global keyword
    
    # Check if new high score
    if score > high_score:
        high_score = score  # Bug 4: Missing global keyword
```

**Instructions:**
1. Identify all bugs (there are 4)
2. Fix each bug
3. Add comments explaining what was wrong
4. Test your fixed code

---

### Problem 3: Extend the Health System (Add to Existing Program)

**Task:** The following program has a basic health system. Extend it by adding the requested features.

```python
# Basic health system
WIDTH = 800
HEIGHT = 600

# Player variables
player_health = 100
max_health = 100

def draw():
    screen.fill((50, 50, 50))  # Gray background
    
    # Draw health bar background
    screen.draw.filled_rect(Rect(10, 10, 200, 30), "red")
    
    # Draw current health
    health_width = (player_health / max_health) * 200
    screen.draw.filled_rect(Rect(10, 10, health_width, 30), "green")
    
    # Draw health text
    screen.draw.text(f"Health: {player_health}/{max_health}", (15, 15), color="white")

def update():
    global player_health
    # Simulate damage over time
    player_health -= 1
    
    # Prevent health from going below 0
    if player_health < 0:
        player_health = 0
```

**Your Tasks:**
1. Add a variable `armor` that starts at 50
2. Add a variable `shield_active` (boolean) that starts as True
3. Modify the damage calculation: if `shield_active` is True, reduce damage by half
4. When `armor` reaches 0, set `shield_active` to False
5. Display the armor value on screen
6. Display shield status on screen (e.g., "Shield: Active" or "Shield: Down")

**Bonus Challenge:** Make the health regenerate slowly when it's below 50 and shield is active.

---

## Project Task: Create a Scoring System Using Global Variables

### Project Description

Build a simple game that demonstrates your understanding of variables by implementing a complete scoring system.

### Requirements

Your game must include:

1. **Window Setup:**
   - WIDTH and HEIGHT constants
   - Background color

2. **Player Variables:**
   - Position (x, y)
   - Speed
   - Size

3. **Game State Variables:**
   - Current score
   - High score
   - Lives remaining
   - Current level

4. **Collectible Variables:**
   - Position of at least one collectible item
   - Point value of collectible

5. **Game Logic:**
   - Player can move (use keyboard input in Module 7, or auto-move for now)
   - When player reaches collectible, score increases
   - Collectible respawns at a new location
   - Display all game state variables on screen

6. **Visual Feedback:**
   - Different colors for player and collectible
   - Score display updates in real-time
   - Visual indication when score increases

### Starter Template

```python
# scoring_game.py
import random

WIDTH = 800
HEIGHT = 600

# TODO: Define your variables here
# Player variables
# Game state variables
# Collectible variables

def draw():
    # TODO: Implement drawing
    pass

def update():
    # TODO: Implement game logic
    pass
```

### Assessment Criteria

- **Variables (40%)**: Appropriate variables defined with meaningful names
- **Game Logic (30%)**: Scoring system works correctly
- **Visual Display (20%)**: All important information displayed clearly
- **Code Quality (10%)**: Code is organized, commented, and follows Python conventions

### Extension Ideas

- Add a timer (use a frame counter variable)
- Implement multiple collectible types with different point values
- Add a "combo multiplier" that increases when collecting items quickly
- Create difficulty levels that affect speed or point values

---

## Key Takeaways

1. **Variables store game state** - Everything in your game that changes is stored in variables
2. **Meaningful names matter** - `player_x` is better than `x` or `p1`
3. **Global vs. Local** - Understanding scope is crucial for game development
4. **Abstraction** - Variables let us think about game concepts rather than memory locations
5. **Data types** - Different types (int, float, string, bool) serve different purposes

## Additional Resources

- Python Variables Documentation
- Pygame Zero Documentation: Drawing and Update Functions
- AP CSP Reference Sheet: Variables and Assignment

## Next Module

In Module 2, we'll learn about **Conditionals and Game Logic**, exploring how to make decisions in our games using if statements and Boolean logic.
