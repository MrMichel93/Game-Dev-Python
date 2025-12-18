# Module 3: Loops and Animation

## Learning Objectives
- Apply loops to create repeated actions and animations
- Use iteration to process collections of game objects
- Understand how loops enable efficient code through repetition
- Recognize loops as abstractions that simplify repetitive tasks

## AP CSP Alignment

**Big Idea:** Algorithms and Programming (AAP)

**Specific Standards:**
- AAP-2.K.1: Iteration is a repeating portion of an algorithm
- AAP-2.K.2: Iteration repeats until a condition is met or for a specified number of times
- AAP-2.L: Compare multiple algorithms to determine if they yield the same result
- AAP-2.M: Determine the result of code segments that use iteration

**Computational Thinking Practices:**
- 2.B: Implement and apply an algorithm
- 4.B: Determine the result of code segments

## Concept: Loops in Game Development

### What are Loops?

Loops allow code to repeat multiple times without writing the same code over and over. In games, loops are used for animation, updating multiple objects, drawing backgrounds, and processing user input over time.

### Key Concepts:

1. **For Loops - Definite Iteration**
```python
# Draw a row of stars
for i in range(10):
    x = 50 + i * 60
    screen.draw.filled_circle((x, 100), 20, "yellow")

# Animate particle effects
for particle in particles:
    particle.y += particle.speed
    particle.alpha -= 5
```

2. **While Loops - Indefinite Iteration**
```python
# Spawn enemies until limit reached
enemy_count = 0
while enemy_count < max_enemies:
    spawn_enemy()
    enemy_count += 1

# Process input until game ends
while game_running:
    handle_events()
    update_game()
    draw_screen()
```

3. **Range Function**
```python
# range(stop) - 0 to stop-1
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

# range(start, stop) - start to stop-1
for i in range(2, 7):  # 2, 3, 4, 5, 6
    print(i)

# range(start, stop, step)
for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)
```

4. **Nested Loops**
```python
# Create a grid of tiles
for row in range(10):
    for col in range(10):
        x = col * 50
        y = row * 50
        screen.draw.rect(Rect(x, y, 50, 50), "white")
```

### Loops as Abstraction

Loops abstract the concept of repetition. Instead of writing the same code 100 times, we write it once and loop 100 times. This abstraction:
- Reduces code duplication
- Makes code easier to modify
- Allows for dynamic repetition (runtime-determined counts)
- Simplifies complex operations

## Mini-Lesson: Animating Stars and Particles

### Example: Starfield Animation

```python
# starfield.py
import random

WIDTH = 800
HEIGHT = 600

# Create list of stars with random positions and speeds
stars = []
for i in range(100):
    star = {
        'x': random.randint(0, WIDTH),
        'y': random.randint(0, HEIGHT),
        'speed': random.uniform(0.5, 3.0),
        'size': random.randint(1, 3)
    }
    stars.append(star)

def draw():
    screen.fill((0, 0, 20))  # Dark blue space
    
    # Draw all stars using a loop
    for star in stars:
        screen.draw.filled_circle(
            (int(star['x']), int(star['y'])),
            star['size'],
            "white"
        )
    
    # Display star count
    screen.draw.text(f"Stars: {len(stars)}", 
                    (10, 10), color="white", fontsize=25)

def update():
    # Update all stars using a loop
    for star in stars:
        # Move star down
        star['y'] += star['speed']
        
        # Reset star to top when it goes off bottom
        if star['y'] > HEIGHT:
            star['y'] = 0
            star['x'] = random.randint(0, WIDTH)
```

## Practice Problems

### Problem 1: Create a Grid-Based Game Board (Write All Code)

**Task:** Create a checkerboard pattern using nested loops.

**Requirements:**
1. Create an 8x8 grid of squares
2. Alternate colors (black and red) in checkerboard pattern
3. Each square should be 60x60 pixels
4. Add row and column numbers (0-7) as labels
5. Highlight a square that moves across the board each frame

**Starter Code Structure:**
```python
WIDTH = 480  # 8 * 60
HEIGHT = 480

# Define your variables

def draw():
    # Use nested loops to draw grid
    pass

def update():
    # Update highlighted square position
    pass
```

**Expected Output:** An 8x8 checkerboard with alternating colors and a moving highlight.

---

### Problem 2: Debug the Particle System (Debug and Fix)

**Task:** This particle effect has several bugs. Find and fix them.

```python
# Buggy particle system
import random

WIDTH = 800
HEIGHT = 600

particles = []

def draw():
    screen.fill((0, 0, 0))
    
    # Draw all particles
    for particle in particles:
        screen.draw.filled_circle(
            (particle['x'], particle['y']),
            particle['size'],
            particle['color']
        )
    
    screen.draw.text(f"Particles: {len(particles)}", 
                    (10, 10), color="white")

def update():
    # Spawn new particles
    for i in range(5):  # Bug 1: Spawns too many, should be in condition
        particle = {
            'x': WIDTH / 2,
            'y': HEIGHT / 2,
            'speed_x': random.uniform(-3, 3),
            'speed_y': random.uniform(-3, 3),
            'size': random.randint(2, 5),
            'color': "red"
        }
        particles.append(particle)
    
    # Update particles
    for particle in particles:
        particle['x'] += particle['speed_x']
        particle['y'] += particle['speed_y']
        particle['size'] += 1  # Bug 2: Size increases instead of decreases
    
    # Remove old particles - Bug 3: Modifying list while iterating
    for particle in particles:
        if particle['size'] <= 0:
            particles.remove(particle)
```

**Instructions:**
1. Fix Bug 1: Only spawn particles occasionally (use frame counter)
2. Fix Bug 2: Particles should shrink, not grow
3. Fix Bug 3: Safely remove particles (use list comprehension or iterate backwards)
4. Add Bug 4 fix: Remove particles that go off screen

---

### Problem 3: Extend the Animation System (Add to Existing Program)

**Task:** Extend this simple animation with more features.

```python
# Simple bouncing balls
import random

WIDTH = 800
HEIGHT = 600

balls = []

# Create initial balls
for i in range(5):
    ball = {
        'x': random.randint(50, WIDTH - 50),
        'y': random.randint(50, HEIGHT - 50),
        'speed_x': random.uniform(-3, 3),
        'speed_y': random.uniform(-3, 3),
        'size': 20,
        'color': "blue"
    }
    balls.append(ball)

def draw():
    screen.fill((200, 200, 200))
    
    for ball in balls:
        screen.draw.filled_circle(
            (int(ball['x']), int(ball['y'])),
            ball['size'],
            ball['color']
        )

def update():
    for ball in balls:
        # Move ball
        ball['x'] += ball['speed_x']
        ball['y'] += ball['speed_y']
        
        # Bounce off edges
        if ball['x'] <= ball['size'] or ball['x'] >= WIDTH - ball['size']:
            ball['speed_x'] *= -1
        if ball['y'] <= ball['size'] or ball['y'] >= HEIGHT - ball['size']:
            ball['speed_y'] *= -1
```

**Your Tasks:**
1. Add random colors to balls (use a list of color options)
2. Add gravity effect (increase speed_y each frame)
3. Add ball trails (draw previous positions with fading alpha)
4. Implement ball-to-ball collision detection and response
5. Add ability to spawn new ball on mouse click

**Bonus Challenge:** Add different sizes with different physics properties.

---

## Project Task: Create a Rain/Snow Particle Effect

### Project Description

Build a weather particle system that demonstrates loops and animation principles.

### Requirements

1. **Particle System:**
   - At least 100 particles
   - Each particle has: position, speed, size, and optional properties
   - Use loops to initialize particles

2. **Animation:**
   - Particles fall from top of screen
   - Use loops to update all particles each frame
   - Particles reset to top when reaching bottom

3. **Variety:**
   - Different speeds for particles
   - Different sizes for particles
   - Optional: Different colors/opacity

4. **Visual Polish:**
   - Smooth animation
   - Nice color scheme
   - Particle count display

5. **Enhancements (choose at least 2):**
   - Wind effect (horizontal movement)
   - Ground accumulation (particles pile up)
   - Splash/bounce effect on ground
   - Mouse interaction (particles avoid cursor)
   - Toggle between rain/snow modes

### Starter Template

```python
# weather_particles.py
import random

WIDTH = 800
HEIGHT = 600

# Initialize particles using a loop
particles = []

def draw():
    # Use loop to draw all particles
    pass

def update():
    # Use loop to update all particles
    pass
```

### Assessment Criteria

- **Loop Usage (40%)**: Effective use of for loops for initialization and updates
- **Animation Quality (30%)**: Smooth, visually appealing particle movement
- **Code Organization (15%)**: Clean, well-structured code
- **Enhancements (15%)**: Implementation of creative features

### Extension Ideas

- Multiple particle layers at different depths
- Lighting effects (lightning for rain)
- Day/night cycle affecting particle visibility
- Seasonal transitions (rain to snow)
- Interactive elements (umbrella that blocks rain)

---

## Key Takeaways

1. **Loops enable repetition** - Essential for handling multiple game objects
2. **For loops** - Use when you know the count
3. **While loops** - Use for condition-based repetition
4. **Nested loops** - Create grids and multi-dimensional structures
5. **List iteration** - Process collections efficiently
6. **Abstraction** - Loops simplify repetitive code

## Additional Resources

- Python Loops Documentation
- Animation Principles in Programming
- AP CSP Reference Sheet: Iteration

## Next Module

In Module 4, we'll explore **Lists and Sprite Management**, learning how to effectively manage collections of game objects.
