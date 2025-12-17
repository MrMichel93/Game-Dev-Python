# Module 2: Conditionals and Game Logic

## Learning Objectives
- Apply conditional statements to control game behavior
- Use Boolean logic to make complex game decisions
- Understand how conditionals create branching paths in program execution
- Recognize conditionals as abstractions for decision-making

## AP CSP Alignment

**Big Idea:** Algorithms and Programming (AAP)

**Specific Standards:**
- AAP-2.E: Evaluate expressions that use relational operators
- AAP-2.F: Evaluate expressions that use logic operators
- AAP-2.H: Determine the result of conditional statements
- AAP-2.K: Express an algorithm that uses sequencing without using a programming language

**Computational Thinking Practices:**
- 2.B: Implement and apply an algorithm
- 4.B: Determine the result of code segments

## Concept: Conditionals in Game Development

### What are Conditionals?

Conditionals allow programs to make decisions and execute different code based on conditions. In games, conditionals control everything from character movement to collision detection to game state transitions.

### Key Concepts:

1. **Basic If Statements**
```python
# Check if player is at screen edge
if player_x > WIDTH:
    player_x = 0

# Check if game is over
if lives <= 0:
    game_over = True
```

2. **If-Elif-Else Chains**
```python
# Determine difficulty based on score
if score < 100:
    difficulty = "Easy"
elif score < 500:
    difficulty = "Medium"
elif score < 1000:
    difficulty = "Hard"
else:
    difficulty = "Expert"
```

3. **Boolean Operators**
```python
# AND: Both conditions must be true
if player_x > 0 and player_x < WIDTH:
    # Player is within horizontal bounds
    
# OR: At least one condition must be true
if health <= 0 or time_remaining <= 0:
    game_over = True
    
# NOT: Inverts the condition
if not game_paused:
    update_game_state()
```

4. **Comparison Operators**
```python
# Equal to
if score == high_score:
    show_celebration()

# Not equal to
if current_level != max_level:
    allow_level_up()

# Greater than, less than
if player_health > 50:
    health_status = "Good"
if enemy_distance < 100:
    enemy_attack()
```

### Conditionals as Abstraction

Conditionals abstract the concept of decision-making. Instead of thinking about memory states and jump instructions (low-level), we think about logical conditions (high-level). This abstraction allows us to:
- Express game rules clearly
- Make code self-documenting
- Reason about program behavior intuitively

## Mini-Lesson: Game Boundaries and Collision Detection

### Example: Boundary Checking

```python
# boundary_demo.py
WIDTH = 800
HEIGHT = 600

# Player state
player_x = 400
player_y = 300
player_size = 30
player_speed = 5

# Movement flags
move_left = False
move_right = False
move_up = False
move_down = False

def draw():
    screen.fill((0, 100, 0))  # Green background
    
    # Draw boundaries
    screen.draw.rect(Rect(0, 0, WIDTH, HEIGHT), "white")
    
    # Change color if at boundary
    color = "red" if is_at_boundary() else "blue"
    screen.draw.filled_circle((player_x, player_y), player_size, color)
    
    # Display position
    screen.draw.text(f"Position: ({player_x}, {player_y})", 
                    (10, 10), color="white", fontsize=25)

def update():
    global player_x, player_y
    
    # Try to move
    new_x = player_x
    new_y = player_y
    
    if move_left:
        new_x -= player_speed
    if move_right:
        new_x += player_speed
    if move_up:
        new_y -= player_speed
    if move_down:
        new_y += player_speed
    
    # Only update position if within boundaries
    if new_x >= player_size and new_x <= WIDTH - player_size:
        player_x = new_x
    if new_y >= player_size and new_y <= HEIGHT - player_size:
        player_y = new_y

def is_at_boundary():
    """Check if player is touching any boundary"""
    return (player_x <= player_size or 
            player_x >= WIDTH - player_size or
            player_y <= player_size or
            player_y >= HEIGHT - player_size)

def on_key_down(key):
    global move_left, move_right, move_up, move_down
    if key == keys.LEFT:
        move_left = True
    elif key == keys.RIGHT:
        move_right = True
    elif key == keys.UP:
        move_up = True
    elif key == keys.DOWN:
        move_down = True

def on_key_up(key):
    global move_left, move_right, move_up, move_down
    if key == keys.LEFT:
        move_left = False
    elif key == keys.RIGHT:
        move_right = False
    elif key == keys.UP:
        move_up = False
    elif key == keys.DOWN:
        move_down = False
```

## Practice Problems

### Problem 1: Score-Based Difficulty System (Write All Code)

**Task:** Create a game that adjusts difficulty based on the player's score. 

**Requirements:**
1. Start with a score of 0 and a base speed of 2
2. Use conditionals to adjust game speed based on score:
   - Score 0-99: Speed = 2 (Easy)
   - Score 100-299: Speed = 4 (Medium)
   - Score 300-499: Speed = 6 (Hard)
   - Score 500+: Speed = 8 (Expert)
3. Display current difficulty level as text
4. Automatically increase score each frame
5. Show different background colors for each difficulty level

**Starter Code Structure:**
```python
WIDTH = 800
HEIGHT = 600

# Define your variables

def draw():
    # Your drawing code
    pass

def update():
    # Your game logic with conditionals
    pass
```

**Expected Behavior:** As the score increases, the difficulty level changes and the game speed increases.

---

### Problem 2: Debug the Collision System (Debug and Fix)

**Task:** This collision detection system has bugs. Find and fix all issues.

```python
# Buggy collision detection
WIDTH = 800
HEIGHT = 600

player_x = 100
player_y = 100
player_size = 30

enemy_x = 400
enemy_y = 300
enemy_size = 25

collision_detected = False

def draw():
    screen.fill((0, 0, 0))
    
    # Draw player
    screen.draw.filled_circle((player_x, player_y), player_size, "blue")
    
    # Draw enemy
    screen.draw.filled_circle((enemy_x, enemy_y), enemy_size, "red")
    
    # Show collision status
    if collision_detected == True:  # Bug 1: Redundant comparison
        screen.draw.text("COLLISION!", (WIDTH/2 - 50, 50), color="yellow", fontsize=40)

def update():
    global player_x, collision_detected
    
    # Move player toward enemy
    player_x += 2
    
    # Check collision
    distance = ((player_x - enemy_x) ** 2 + (player_y - enemy_y) ** 2) ** 0.5
    
    # Bug 2: Wrong comparison operator
    if distance > player_size + enemy_size:
        collision_detected = True
    else:
        collision_detected = False  # Bug 3: Logic should be opposite
    
    # Bug 4: No bounds checking - player goes off screen
```

**Instructions:**
1. Identify all 4 bugs
2. Fix the collision detection logic
3. Add proper bounds checking
4. Add comments explaining your fixes

---

### Problem 3: Extend the Game State Manager (Add to Existing Program)

**Task:** The following program manages basic game states. Extend it with new features.

```python
# Basic game state manager
WIDTH = 800
HEIGHT = 600

# Game states
STATE_MENU = "menu"
STATE_PLAYING = "playing"
STATE_PAUSED = "paused"
STATE_GAME_OVER = "game_over"

current_state = STATE_MENU
score = 0
lives = 3

def draw():
    if current_state == STATE_MENU:
        screen.fill((0, 0, 100))
        screen.draw.text("MENU - Press SPACE to Start", 
                        (WIDTH/2 - 150, HEIGHT/2), 
                        color="white", fontsize=30)
    
    elif current_state == STATE_PLAYING:
        screen.fill((0, 100, 0))
        screen.draw.text(f"Score: {score}  Lives: {lives}", 
                        (10, 10), color="white", fontsize=25)
        screen.draw.text("Playing... Press P to Pause", 
                        (WIDTH/2 - 120, HEIGHT/2), 
                        color="white", fontsize=20)
    
    elif current_state == STATE_GAME_OVER:
        screen.fill((100, 0, 0))
        screen.draw.text("GAME OVER", 
                        (WIDTH/2 - 80, HEIGHT/2), 
                        color="white", fontsize=40)

def update():
    global score, lives, current_state
    
    if current_state == STATE_PLAYING:
        score += 1
        
        # Simulate losing lives
        if score % 500 == 0 and score > 0:
            lives -= 1
        
        # Check game over
        if lives <= 0:
            current_state = STATE_GAME_OVER

def on_key_down(key):
    global current_state
    
    if key == keys.SPACE and current_state == STATE_MENU:
        current_state = STATE_PLAYING
```

**Your Tasks:**
1. Add the `STATE_PAUSED` functionality:
   - Press P to pause during gameplay
   - Display "PAUSED - Press P to Resume" message
   - Press P again to resume
2. Add a high score system:
   - Track high score across game sessions (within the program)
   - Display high score on menu and game over screens
3. Add a "win condition":
   - If score reaches 2000, change to a new STATE_WIN
   - Create a win screen with appropriate message
4. Add state transitions from game over:
   - Press R to restart (reset score and lives, go to menu)

**Bonus Challenge:** Add different difficulty levels that can be selected from the menu.

---

## Project Task: Build a Traffic Light Game

### Project Description

Create a simple reaction-time game using conditional logic. A traffic light changes colors, and players must respond correctly.

### Requirements

1. **Traffic Light System:**
   - Three states: RED, YELLOW, GREEN
   - Light changes automatically after random intervals
   - Display current light color prominently

2. **Game Rules (using conditionals):**
   - RED: Player must stop (not press any key)
   - YELLOW: Player should prepare (can press any key, no penalty)
   - GREEN: Player must GO (press SPACE to score points)
   - Pressing SPACE on RED: Lose a life
   - Not pressing SPACE fast enough on GREEN: Lose a life

3. **Game State Variables:**
   - Current light color
   - Score
   - Lives (start with 3)
   - Timer for light changes
   - Reaction time tracking

4. **Visual Design:**
   - Clear visual representation of traffic light
   - Score and lives display
   - Instructions for player
   - Game over screen

5. **Conditional Logic Requirements:**
   - Use if-elif-else for state management
   - Use Boolean operators for complex conditions
   - Implement proper collision/input validation
   - Handle game over conditions

### Starter Template

```python
# traffic_light_game.py
import random

WIDTH = 800
HEIGHT = 600

# Traffic light states
RED = "red"
YELLOW = "yellow"
GREEN = "green"

# TODO: Define your game variables

def draw():
    # TODO: Implement drawing
    pass

def update():
    # TODO: Implement game logic with conditionals
    pass

def on_key_down(key):
    # TODO: Handle player input
    pass
```

### Assessment Criteria

- **Conditional Logic (40%)**: Proper use of if-elif-else and Boolean operators
- **Game Rules (30%)**: Correctly implements traffic light behavior
- **User Experience (20%)**: Clear visuals and feedback
- **Code Quality (10%)**: Well-organized, commented code

### Extension Ideas

- Add score multipliers for fast reactions
- Include a "combo" system for consecutive correct responses
- Add sound effects for correct/incorrect actions
- Implement increasing difficulty (faster light changes)
- Add a leaderboard system

---

## Key Takeaways

1. **Conditionals enable decision-making** - They're essential for game logic
2. **Boolean logic creates complex conditions** - Combine simple checks for sophisticated behavior
3. **State management** - Use conditionals to control game flow
4. **Abstraction** - Conditionals let us express rules clearly
5. **Testing edge cases** - Always consider boundary conditions

## Additional Resources

- Python Conditionals Documentation
- Boolean Logic Tutorial
- AP CSP Reference Sheet: Conditionals and Boolean Logic

## Next Module

In Module 3, we'll explore **Loops and Animation**, learning how to create repeated actions and smooth animations in our games.
