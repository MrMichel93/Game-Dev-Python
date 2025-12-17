# Module 8: Collision Detection and Game Physics

## Learning Objectives
- Implement various collision detection algorithms
- Apply basic physics principles in game development
- Optimize collision checking for performance
- Understand how algorithms solve geometric problems

## AP CSP Alignment

**Big Idea:** Algorithms and Programming (AAP)

**Specific Standards:**
- AAP-2.A: Express an algorithm that uses sequencing without using a programming language
- AAP-2.B: Represent a step-by-step algorithmic process
- AAP-2.O: Write iteration statements to traverse lists
- AAP-4.A: Determine the efficiency of an algorithm

**Computational Thinking Practices:**
- 2.B: Implement algorithms
- 4.A: Explain how algorithms work
- 4.B: Determine the result of code segments

## Concept: Collision Detection in Game Development

### What is Collision Detection?

Collision detection determines when game objects intersect or touch. It's fundamental to gameplay—without it, objects pass through each other without interaction.

### Key Concepts:

1. **Circle Collision**
```python
def circles_collide(circle1, circle2):
    """Check if two circles overlap"""
    dx = circle2['x'] - circle1['x']
    dy = circle2['y'] - circle1['y']
    distance = (dx**2 + dy**2)**0.5
    return distance < circle1['radius'] + circle2['radius']
```

2. **Rectangle Collision (AABB)**
```python
def rects_collide(rect1, rect2):
    """Axis-Aligned Bounding Box collision"""
    return (rect1['x'] < rect2['x'] + rect2['width'] and
            rect1['x'] + rect1['width'] > rect2['x'] and
            rect1['y'] < rect2['y'] + rect2['height'] and
            rect1['y'] + rect1['height'] > rect2['y'])
```

3. **Point-in-Shape**
```python
def point_in_circle(px, py, circle):
    """Check if point is inside circle"""
    dx = px - circle['x']
    dy = py - circle['y']
    return (dx**2 + dy**2)**0.5 < circle['radius']

def point_in_rect(px, py, rect):
    """Check if point is inside rectangle"""
    return (rect['x'] <= px <= rect['x'] + rect['width'] and
            rect['y'] <= py <= rect['y'] + rect['height'])
```

4. **Collision Response**
```python
def handle_collision(obj1, obj2):
    """Resolve collision between objects"""
    # Calculate collision normal
    dx = obj2['x'] - obj1['x']
    dy = obj2['y'] - obj1['y']
    distance = (dx**2 + dy**2)**0.5
    
    # Normalize
    nx = dx / distance
    ny = dy / distance
    
    # Separate objects
    overlap = (obj1['radius'] + obj2['radius']) - distance
    obj1['x'] -= nx * overlap * 0.5
    obj1['y'] -= ny * overlap * 0.5
    obj2['x'] += nx * overlap * 0.5
    obj2['y'] += ny * overlap * 0.5
    
    # Bounce (simple reflection)
    obj1['vx'], obj2['vx'] = obj2['vx'], obj1['vx']
    obj1['vy'], obj2['vy'] = obj2['vy'], obj1['vy']
```

### Physics Concepts:

1. **Velocity and Position**
```python
# Basic physics update
position_x += velocity_x
position_y += velocity_y
```

2. **Acceleration and Gravity**
```python
# Apply acceleration
velocity_y += gravity
velocity_x += acceleration_x

# Update position
position_x += velocity_x
position_y += velocity_y
```

3. **Friction and Drag**
```python
# Apply friction
velocity_x *= friction_coefficient  # e.g., 0.98
velocity_y *= friction_coefficient
```

### Algorithms as Problem Solving

Collision detection is a classic algorithmic problem:
- **Efficiency matters**: Checking every object against every other is O(n²)
- **Spatial partitioning**: Divide space into grids to reduce checks
- **Bounding boxes**: Use simple shapes for initial tests
- **Optimization**: Only check nearby objects

## Mini-Lesson: Building a Physics Sandbox

### Example: Bouncing Balls with Collision

```python
# physics_sandbox.py
import random
import math

WIDTH = 800
HEIGHT = 600

GRAVITY = 0.5
FRICTION = 0.99
BOUNCE = 0.8  # Energy retained on bounce

balls = []

def create_ball(x, y):
    """Create a new ball with random properties"""
    return {
        'x': x,
        'y': y,
        'vx': random.uniform(-5, 5),
        'vy': random.uniform(-5, 5),
        'radius': random.randint(15, 30),
        'mass': random.randint(1, 5),
        'color': random.choice(['red', 'blue', 'green', 'yellow', 'purple'])
    }

def draw():
    screen.fill((240, 240, 240))
    
    # Draw ground
    screen.draw.filled_rect(Rect(0, HEIGHT - 50, WIDTH, 50), "brown")
    
    # Draw balls
    for ball in balls:
        screen.draw.filled_circle(
            (int(ball['x']), int(ball['y'])),
            ball['radius'],
            ball['color']
        )
        
        # Show velocity vector
        screen.draw.line(
            (ball['x'], ball['y']),
            (ball['x'] + ball['vx'] * 5, ball['y'] + ball['vy'] * 5),
            "black"
        )
    
    # Instructions
    screen.draw.text("Click to add balls", (10, 10), color="black", fontsize=25)
    screen.draw.text(f"Balls: {len(balls)}", (10, 40), color="black", fontsize=25)

def update():
    # Update each ball
    for ball in balls:
        # Apply physics
        ball['vy'] += GRAVITY
        ball['vx'] *= FRICTION
        ball['vy'] *= FRICTION
        
        # Update position
        ball['x'] += ball['vx']
        ball['y'] += ball['vy']
        
        # Wall collisions
        if ball['x'] - ball['radius'] < 0:
            ball['x'] = ball['radius']
            ball['vx'] = abs(ball['vx']) * BOUNCE
        elif ball['x'] + ball['radius'] > WIDTH:
            ball['x'] = WIDTH - ball['radius']
            ball['vx'] = -abs(ball['vx']) * BOUNCE
        
        # Ground collision
        if ball['y'] + ball['radius'] > HEIGHT - 50:
            ball['y'] = HEIGHT - 50 - ball['radius']
            ball['vy'] = -abs(ball['vy']) * BOUNCE
            
            # Stop if moving very slowly
            if abs(ball['vy']) < 0.5:
                ball['vy'] = 0
    
    # Ball-to-ball collision
    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            check_ball_collision(balls[i], balls[j])

def check_ball_collision(ball1, ball2):
    """Check and resolve collision between two balls"""
    dx = ball2['x'] - ball1['x']
    dy = ball2['y'] - ball1['y']
    distance = math.sqrt(dx**2 + dy**2)
    
    min_distance = ball1['radius'] + ball2['radius']
    
    if distance < min_distance:
        # Normalize collision vector
        nx = dx / distance
        ny = dy / distance
        
        # Separate balls
        overlap = min_distance - distance
        ball1['x'] -= nx * overlap * 0.5
        ball1['y'] -= ny * overlap * 0.5
        ball2['x'] += nx * overlap * 0.5
        ball2['y'] += ny * overlap * 0.5
        
        # Calculate relative velocity
        dvx = ball2['vx'] - ball1['vx']
        dvy = ball2['vy'] - ball1['vy']
        
        # Velocity along collision normal
        dot_product = dvx * nx + dvy * ny
        
        # Only resolve if balls moving toward each other
        if dot_product < 0:
            # Mass-based collision response
            total_mass = ball1['mass'] + ball2['mass']
            
            ball1['vx'] += 2 * ball2['mass'] / total_mass * dot_product * nx
            ball1['vy'] += 2 * ball2['mass'] / total_mass * dot_product * ny
            ball2['vx'] -= 2 * ball1['mass'] / total_mass * dot_product * nx
            ball2['vy'] -= 2 * ball1['mass'] / total_mass * dot_product * ny

def on_mouse_down(pos):
    """Add ball at click position"""
    x, y = pos
    balls.append(create_ball(x, y))
```

## Practice Problems

### Problem 1: Platformer Collision System (Write All Code)

**Task:** Create a platformer with proper collision detection.

**Requirements:**
1. Player character (rectangle)
2. At least 3 platforms (rectangles)
3. Gravity affects player
4. Player lands on platforms (stops falling)
5. Player can't pass through platforms from any direction
6. Display collision status

**Expected Structure:**
```python
WIDTH = 800
HEIGHT = 600

player = {
    'x': 100, 'y': 100,
    'width': 30, 'height': 40,
    'vx': 0, 'vy': 0
}

platforms = [
    {'x': 0, 'y': 550, 'width': 800, 'height': 50},
    # Add more platforms
]

def check_platform_collision(player, platform):
    pass
```

---

### Problem 2: Debug the Collision System (Debug and Fix)

**Task:** This collision system has bugs. Fix them.

```python
# Buggy collision system
import math

WIDTH = 800
HEIGHT = 600

player = {'x': 100, 'y': 300, 'radius': 25, 'vx': 3, 'vy': 0}
enemies = [
    {'x': 400, 'y': 300, 'radius': 20},
    {'x': 600, 'y': 350, 'radius': 30}
]
coins = [
    {'x': 300, 'y': 300, 'radius': 15, 'collected': False},
    {'x': 500, 'y': 250, 'radius': 15, 'collected': False}
]

score = 0
game_over = False

def draw():
    screen.fill((50, 50, 50))
    
    if not game_over:
        # Draw player
        screen.draw.filled_circle((int(player['x']), int(player['y'])), 
                                 player['radius'], "blue")
        
        # Draw enemies
        for enemy in enemies:
            screen.draw.filled_circle((enemy['x'], enemy['y']), 
                                     enemy['radius'], "red")
        
        # Draw coins
        for coin in coins:
            if not coin['collected']:
                screen.draw.filled_circle((coin['x'], coin['y']), 
                                         coin['radius'], "yellow")
    else:
        screen.draw.text("GAME OVER", (WIDTH/2 - 80, HEIGHT/2), 
                        color="red", fontsize=50)
    
    screen.draw.text(f"Score: {score}", (10, 10), color="white", fontsize=30)

def update():
    global score, game_over
    
    if game_over:
        return
    
    # Move player
    player['x'] += player['vx']
    
    # Wrap around screen - Bug 1: Should wrap at edges
    if player['x'] > WIDTH:
        player['x'] = WIDTH  # Should be 0
    
    # Check coin collisions
    for coin in coins:
        # Bug 2: Wrong distance calculation
        distance = abs(player['x'] - coin['x']) + abs(player['y'] - coin['y'])
        
        if distance < player['radius'] + coin['radius']:
            coin['collected'] = True
            score += 10
    
    # Check enemy collisions - Bug 3: Not checking all enemies
    enemy = enemies[0]
    dx = player['x'] - enemy['x']
    dy = player['y'] - enemy['y']
    distance = math.sqrt(dx**2 + dy**2)
    
    # Bug 4: Wrong comparison
    if distance > player['radius'] + enemy['radius']:
        game_over = True
```

---

### Problem 3: Extend the Physics Engine (Add to Existing Program)

**Task:** Extend this simple physics engine.

```python
# Basic physics engine
import math

WIDTH = 800
HEIGHT = 600

GRAVITY = 0.3

objects = []

def create_box(x, y, width, height):
    return {
        'type': 'box',
        'x': x, 'y': y,
        'width': width, 'height': height,
        'vx': 0, 'vy': 0,
        'mass': width * height / 100
    }

def update_physics():
    for obj in objects:
        # Apply gravity
        obj['vy'] += GRAVITY
        
        # Update position
        obj['x'] += obj['vx']
        obj['y'] += obj['vy']
        
        # Ground collision
        if obj['y'] + obj['height'] > HEIGHT:
            obj['y'] = HEIGHT - obj['height']
            obj['vy'] = -obj['vy'] * 0.6
```

**Your Tasks:**
1. Add rotation to objects (angle and angular velocity)
2. Add air resistance (slows down objects over time)
3. Implement object-to-object collision with proper physics response
4. Add different material properties (bounciness, friction)
5. Add explosions that apply force to nearby objects
6. Implement joints/constraints between objects

---

## Project Task: Create a Brick Breaker Game

### Project Description

Build a complete brick breaker game with physics and collision detection.

### Requirements

1. **Game Objects:**
   - Paddle (player controlled, rectangle)
   - Ball (moves with velocity, circle)
   - Bricks (grid of rectangles, multiple rows/colors)
   - Walls (screen boundaries)

2. **Collision Detection:**
   - Ball-paddle collision (reflects ball, angle depends on hit position)
   - Ball-brick collision (destroys brick, reflects ball)
   - Ball-wall collision (reflects ball)
   - Ball-bottom collision (lose life)

3. **Physics:**
   - Ball has velocity (vx, vy)
   - Ball speed increases slightly over time
   - Accurate reflection angles
   - Paddle can influence ball direction

4. **Game Mechanics:**
   - Multiple lives
   - Score system (different bricks worth different points)
   - Level progression (clear all bricks)
   - Power-ups (optional: multi-ball, larger paddle, etc.)

5. **Visual Feedback:**
   - Brick destruction effects
   - Ball trail
   - Score display
   - Lives display

### Starter Template

```python
# brick_breaker.py
WIDTH = 800
HEIGHT = 600

paddle = {
    'x': WIDTH // 2,
    'y': HEIGHT - 50,
    'width': 100,
    'height': 20
}

ball = {
    'x': WIDTH // 2,
    'y': HEIGHT // 2,
    'vx': 5,
    'vy': -5,
    'radius': 10
}

bricks = []

def create_bricks():
    pass

def check_ball_paddle_collision():
    pass

def check_ball_brick_collisions():
    pass

def update_ball_physics():
    pass
```

### Assessment Criteria

- **Collision Detection (40%)**: Accurate, responsive collision system
- **Physics (25%)**: Realistic ball movement and reflection
- **Game Mechanics (20%)**: Complete, balanced gameplay
- **Code Quality (15%)**: Clean, efficient code

### Extension Ideas

- Different brick types (multiple hits, moving, etc.)
- Power-ups that fall from destroyed bricks
- Curved ball trajectory
- Particle effects
- Level editor

---

## Key Takeaways

1. **Collision detection is algorithmic** - Choose the right algorithm for the situation
2. **Shape matters** - Different shapes need different algorithms
3. **Physics simulation** - Velocity, acceleration, forces
4. **Performance** - Optimize collision checks for many objects
5. **Response is crucial** - Detecting collision is just the first step
6. **Abstraction** - Hide complex math behind simple functions

## Additional Resources

- Collision Detection Algorithms
- Game Physics Tutorial
- AP CSP Reference Sheet: Algorithms and Efficiency

## Next Module

In Module 9, we'll explore **Game Design and Creative Development**, applying creative thinking to game development.
