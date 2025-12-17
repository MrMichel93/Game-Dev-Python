# Module 7: Event Handling and User Input

## Learning Objectives
- Handle keyboard and mouse events in games
- Implement responsive controls for player interaction
- Understand event-driven programming paradigms
- Apply input validation and state management

## AP CSP Alignment

**Big Idea:** Computer Systems and Networks (CSN)

**Specific Standards:**
- CSN-1.A: Explain how computing devices work together in a network
- CSN-1.B: Explain how the Internet works (conceptual: input/output as communication)
- AAP-3.E: Evaluate expressions that manipulate data in response to events
- IOC-1.A: Explain how computing innovations affect communication

**Computational Thinking Practices:**
- 5.D: Describe the behavior of a program
- 2.B: Implement algorithms that use events

## Concept: Event Handling in Game Development

### What is Event-Driven Programming?

Event-driven programming responds to user actions (events) like key presses, mouse clicks, or mouse movement. Games are inherently event-driven—they constantly listen for and respond to player input.

### Key Concepts:

1. **Keyboard Events in Pygame Zero**
```python
# Key press event (triggered once when key is pressed)
def on_key_down(key):
    if key == keys.SPACE:
        player_jump()
    elif key == keys.E:
        interact_with_object()

# Key release event
def on_key_up(key):
    if key == keys.LEFT:
        stop_moving_left()
```

2. **Continuous Key Checking**
```python
def update():
    # Check if key is currently held down
    if keyboard.left:
        player_x -= player_speed
    if keyboard.right:
        player_x += player_speed
    if keyboard.up:
        player_y -= player_speed
    if keyboard.down:
        player_y += player_speed
```

3. **Mouse Events**
```python
def on_mouse_down(pos, button):
    """Handle mouse button press"""
    mouse_x, mouse_y = pos
    
    if button == mouse.LEFT:
        shoot_projectile(mouse_x, mouse_y)
    elif button == mouse.RIGHT:
        place_building(mouse_x, mouse_y)

def on_mouse_move(pos):
    """Track mouse position"""
    global mouse_x, mouse_y
    mouse_x, mouse_y = pos
```

4. **Input State Management**
```python
# Using flags for input state
input_state = {
    'moving_left': False,
    'moving_right': False,
    'jumping': False,
    'shooting': False
}

def on_key_down(key):
    if key == keys.LEFT:
        input_state['moving_left'] = True
    elif key == keys.SPACE:
        input_state['jumping'] = True

def on_key_up(key):
    if key == keys.LEFT:
        input_state['moving_left'] = False
```

### Event Handling as System Interaction

Event handling represents the interaction between systems (player and game). This connects to the CSN Big Idea:
- **Input devices** (keyboard, mouse) send data to the program
- **Event system** processes and routes events
- **Game logic** responds to events
- **Output devices** (screen) show results

## Mini-Lesson: Creating a Responsive Control System

### Example: Multi-Directional Movement with Mouse Aiming

```python
# player_controls.py
import math

WIDTH = 800
HEIGHT = 600

# Player state
player = {
    'x': WIDTH // 2,
    'y': HEIGHT // 2,
    'speed': 5,
    'angle': 0,  # Angle player is facing
    'size': 30
}

# Input state
keys_pressed = {
    'up': False,
    'down': False,
    'left': False,
    'right': False
}

# Mouse state
mouse_x, mouse_y = WIDTH // 2, HEIGHT // 2

# Projectiles
projectiles = []

def draw():
    screen.fill((30, 30, 30))
    
    # Draw player (triangle pointing toward mouse)
    angle = player['angle']
    points = [
        (player['x'] + math.cos(angle) * player['size'],
         player['y'] + math.sin(angle) * player['size']),
        (player['x'] + math.cos(angle + 2.5) * player['size'] * 0.6,
         player['y'] + math.sin(angle + 2.5) * player['size'] * 0.6),
        (player['x'] + math.cos(angle - 2.5) * player['size'] * 0.6,
         player['y'] + math.sin(angle - 2.5) * player['size'] * 0.6)
    ]
    screen.draw.filled_polygon(points, "blue")
    
    # Draw projectiles
    for proj in projectiles:
        screen.draw.filled_circle((int(proj['x']), int(proj['y'])), 5, "yellow")
    
    # Draw crosshair at mouse
    screen.draw.circle((mouse_x, mouse_y), 10, "red")
    screen.draw.line((mouse_x - 15, mouse_y), (mouse_x + 15, mouse_y), "red")
    screen.draw.line((mouse_x, mouse_y - 15), (mouse_x, mouse_y + 15), "red")

def update():
    # Calculate movement direction
    dx = 0
    dy = 0
    
    if keys_pressed['left']:
        dx -= 1
    if keys_pressed['right']:
        dx += 1
    if keys_pressed['up']:
        dy -= 1
    if keys_pressed['down']:
        dy += 1
    
    # Normalize diagonal movement
    if dx != 0 and dy != 0:
        length = math.sqrt(dx**2 + dy**2)
        dx /= length
        dy /= length
    
    # Apply movement
    player['x'] += dx * player['speed']
    player['y'] += dy * player['speed']
    
    # Keep player on screen
    player['x'] = max(player['size'], min(WIDTH - player['size'], player['x']))
    player['y'] = max(player['size'], min(HEIGHT - player['size'], player['y']))
    
    # Update player angle to face mouse
    player['angle'] = math.atan2(
        mouse_y - player['y'],
        mouse_x - player['x']
    )
    
    # Update projectiles
    for proj in projectiles:
        proj['x'] += proj['vx']
        proj['y'] += proj['vy']
    
    # Remove off-screen projectiles
    projectiles[:] = [p for p in projectiles 
                      if 0 <= p['x'] <= WIDTH and 0 <= p['y'] <= HEIGHT]

def on_key_down(key):
    """Handle key press events"""
    if key == keys.LEFT or key == keys.A:
        keys_pressed['left'] = True
    elif key == keys.RIGHT or key == keys.D:
        keys_pressed['right'] = True
    elif key == keys.UP or key == keys.W:
        keys_pressed['up'] = True
    elif key == keys.DOWN or key == keys.S:
        keys_pressed['down'] = True

def on_key_up(key):
    """Handle key release events"""
    if key == keys.LEFT or key == keys.A:
        keys_pressed['left'] = False
    elif key == keys.RIGHT or key == keys.D:
        keys_pressed['right'] = False
    elif key == keys.UP or key == keys.W:
        keys_pressed['up'] = False
    elif key == keys.DOWN or key == keys.S:
        keys_pressed['down'] = False

def on_mouse_move(pos):
    """Track mouse position"""
    global mouse_x, mouse_y
    mouse_x, mouse_y = pos

def on_mouse_down(pos, button):
    """Handle mouse clicks"""
    if button == mouse.LEFT:
        # Shoot toward mouse
        angle = player['angle']
        projectile = {
            'x': player['x'],
            'y': player['y'],
            'vx': math.cos(angle) * 10,
            'vy': math.sin(angle) * 10
        }
        projectiles.append(projectile)
```

## Practice Problems

### Problem 1: Menu System with Keyboard Navigation (Write All Code)

**Task:** Create a menu system navigable with keyboard.

**Requirements:**
1. Menu with at least 4 options
2. Arrow keys to move selection up/down
3. Enter to select highlighted option
4. Visual highlighting of selected option
5. Each option leads to a different screen/message

**Expected Structure:**
```python
WIDTH = 800
HEIGHT = 600

menu_options = ["Start Game", "Options", "High Scores", "Quit"]
selected_option = 0

def draw():
    # Draw menu with highlighting
    pass

def on_key_down(key):
    # Handle navigation
    pass
```

---

### Problem 2: Debug the Jump Mechanic (Debug and Fix)

**Task:** This jump system has bugs. Fix them.

```python
# Buggy jump system
WIDTH = 800
HEIGHT = 600

player = {
    'x': WIDTH // 2,
    'y': HEIGHT - 50,
    'vy': 0,
    'on_ground': True
}

GRAVITY = 0.5
JUMP_FORCE = -12
GROUND_Y = HEIGHT - 50

def draw():
    screen.fill((100, 150, 255))
    
    # Draw ground
    screen.draw.filled_rect(Rect(0, GROUND_Y + 20, WIDTH, HEIGHT), "green")
    
    # Draw player
    screen.draw.filled_circle((int(player['x']), int(player['y'])), 25, "red")

def update():
    # Apply gravity
    player['vy'] += GRAVITY
    player['y'] += player['vy']
    
    # Check ground collision - Bug 1: Wrong comparison
    if player['y'] > GROUND_Y:
        player['y'] = GROUND_Y
        player['vy'] = 0
        player['on_ground'] = True
    else:
        player['on_ground'] = False  # Bug 2: Should not always set to False

def on_key_down(key):
    if key == keys.SPACE:
        # Bug 3: Can jump in mid-air
        player['vy'] = JUMP_FORCE
        player['on_ground'] = False
        
    # Bug 4: No horizontal movement controls
```

---

### Problem 3: Extend the Click Game (Add to Existing Program)

**Task:** Extend this clicking game with new features.

```python
# Basic clicking game
import random

WIDTH = 800
HEIGHT = 600

target = {
    'x': WIDTH // 2,
    'y': HEIGHT // 2,
    'size': 40
}

score = 0
clicks = 0

def draw():
    screen.fill((200, 200, 200))
    
    # Draw target
    screen.draw.filled_circle((target['x'], target['y']), target['size'], "red")
    screen.draw.circle((target['x'], target['y']), target['size'], "black")
    
    # Draw score
    screen.draw.text(f"Score: {score}", (10, 10), color="black", fontsize=30)
    screen.draw.text(f"Clicks: {clicks}", (10, 45), color="black", fontsize=30)

def on_mouse_down(pos):
    global score, clicks
    mouse_x, mouse_y = pos
    clicks += 1
    
    # Check if clicked on target
    dx = mouse_x - target['x']
    dy = mouse_y - target['y']
    distance = (dx**2 + dy**2)**0.5
    
    if distance <= target['size']:
        score += 10
        # Move target to random position
        target['x'] = random.randint(target['size'], WIDTH - target['size'])
        target['y'] = random.randint(target['size'], HEIGHT - target['size'])
```

**Your Tasks:**
1. Add a timer (60 seconds countdown)
2. Add accuracy display (hits / total clicks)
3. Make target shrink over time (increasing difficulty)
4. Add bonus targets that appear briefly for extra points
5. Add different colored targets worth different points
6. Add keyboard controls to pause/resume game

---

## Project Task: Create a Twin-Stick Shooter Control System

### Project Description

Build a complete control system for a twin-stick shooter (move with WASD, aim/shoot with mouse).

### Requirements

1. **Movement System:**
   - WASD for 8-directional movement
   - Smooth acceleration and deceleration
   - Speed limits
   - Screen boundary handling

2. **Aiming System:**
   - Player faces mouse cursor
   - Visual indicator showing aim direction
   - Crosshair at mouse position

3. **Shooting System:**
   - Left click to shoot
   - Cooldown between shots
   - Bullet spawns at player position
   - Bullets travel toward aim point

4. **Additional Controls:**
   - Spacebar for special ability (dash, shield, etc.)
   - R to reload
   - ESC to pause
   - Tab to show/hide stats

5. **Feedback Systems:**
   - Visual feedback for all inputs
   - Display ammo count
   - Show cooldown timers
   - Display movement speed

### Starter Template

```python
# twin_stick_shooter.py
import math

WIDTH = 800
HEIGHT = 600

player = {}
projectiles = []
input_state = {}

def draw():
    pass

def update():
    pass

def on_key_down(key):
    pass

def on_key_up(key):
    pass

def on_mouse_down(pos, button):
    pass

def on_mouse_move(pos):
    pass
```

### Assessment Criteria

- **Input Handling (40%)**: Responsive, intuitive controls
- **Game Feel (30%)**: Smooth movement, good feedback
- **Feature Completeness (20%)**: All requirements implemented
- **Code Quality (10%)**: Clean, organized code

### Extension Ideas

- Controller support
- Customizable key bindings
- Input buffering for combo moves
- Mouse sensitivity settings
- Alternative control schemes

---

## Key Takeaways

1. **Event-driven programming** - Games respond to user actions
2. **Input state management** - Track what inputs are active
3. **Continuous vs. discrete input** - Held keys vs. single presses
4. **Multiple input sources** - Keyboard, mouse, gamepad
5. **Feedback is essential** - Users need to know their input was received
6. **System interaction** - Input/output as communication

## Additional Resources

- Pygame Zero Input Handling
- Game Input Design Patterns
- AP CSP Reference Sheet: Event Handling

## Next Module

In Module 8, we'll explore **Collision Detection and Game Physics**, learning how to make objects interact realistically.
