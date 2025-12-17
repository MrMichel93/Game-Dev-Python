"""
Module 5 Example: Game Utility Functions Library
Demonstrates how functions create reusable, abstract building blocks
"""
import random
import math

WIDTH = 800
HEIGHT = 600

# ==================== MATH UTILITIES ====================

def distance(x1, y1, x2, y2):
    """Calculate distance between two points"""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def angle_between(x1, y1, x2, y2):
    """Calculate angle from point 1 to point 2 in radians"""
    return math.atan2(y2 - y1, x2 - x1)

def lerp(start, end, t):
    """Linear interpolation between start and end
    t should be between 0 and 1"""
    return start + (end - start) * t

def clamp(value, min_val, max_val):
    """Constrain value between min and max"""
    return max(min_val, min(max_val, value))

# ==================== COLLISION FUNCTIONS ====================

def circle_collision(obj1, obj2):
    """Check collision between two circular objects"""
    dist = distance(obj1['x'], obj1['y'], obj2['x'], obj2['y'])
    return dist < obj1['radius'] + obj2['radius']

def rect_collision(rect1, rect2):
    """Check collision between two rectangles (AABB)"""
    return (rect1['x'] < rect2['x'] + rect2['width'] and
            rect1['x'] + rect1['width'] > rect2['x'] and
            rect1['y'] < rect2['y'] + rect2['height'] and
            rect1['y'] + rect1['height'] > rect2['y'])

def point_in_circle(px, py, circle):
    """Check if point is inside circle"""
    return distance(px, py, circle['x'], circle['y']) < circle['radius']

def point_in_rect(px, py, rect):
    """Check if point is inside rectangle"""
    return (rect['x'] <= px <= rect['x'] + rect['width'] and
            rect['y'] <= py <= rect['y'] + rect['height'])

# ==================== POSITION FUNCTIONS ====================

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

def keep_in_bounds(obj, width=WIDTH, height=HEIGHT):
    """Keep object within screen bounds"""
    obj['x'] = clamp(obj['x'], 0, width)
    obj['y'] = clamp(obj['y'], 0, height)

# ==================== PARTICLE FUNCTIONS ====================

def create_explosion_particles(x, y, count=10, color_list=None):
    """Generate particle data for explosion effect"""
    if color_list is None:
        color_list = ["red", "orange", "yellow"]
    
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
            'max_life': 40,
            'size': random.randint(3, 6),
            'color': random.choice(color_list)
        }
        particles.append(particle)
    return particles

def update_particles(particles):
    """Update all particles and remove dead ones"""
    for particle in particles:
        particle['x'] += particle['vx']
        particle['y'] += particle['vy']
        particle['life'] -= 1
        # Apply gravity
        particle['vy'] += 0.2
    
    # Remove dead particles
    return [p for p in particles if p['life'] > 0]

# ==================== DEMO USAGE ====================

# Example objects
player = {'x': 400, 'y': 300, 'radius': 20}
enemy = {'x': 500, 'y': 350, 'radius': 25}
particles = []

def draw():
    screen.fill((30, 30, 30))
    
    # Draw player
    screen.draw.filled_circle((int(player['x']), int(player['y'])), 
                             player['radius'], "blue")
    
    # Draw enemy
    screen.draw.filled_circle((int(enemy['x']), int(enemy['y'])), 
                             enemy['radius'], "red")
    
    # Draw particles
    for particle in particles:
        alpha_ratio = particle['life'] / particle['max_life']
        size = int(particle['size'] * alpha_ratio)
        if size > 0:
            screen.draw.filled_circle(
                (int(particle['x']), int(particle['y'])),
                size,
                particle['color']
            )
    
    # Draw info
    dist = distance(player['x'], player['y'], enemy['x'], enemy['y'])
    screen.draw.text(f"Distance: {dist:.1f}", (10, 10), 
                    color="white", fontsize=25)
    
    if circle_collision(player, enemy):
        screen.draw.text("COLLISION!", (WIDTH/2 - 80, 50), 
                        color="yellow", fontsize=40)
    
    # Instructions
    screen.draw.text("Arrow keys to move, Space for explosion", 
                    (10, HEIGHT - 30), color="white", fontsize=20)

def update():
    global particles
    
    # Update particles
    particles = update_particles(particles)
    
    # Keep objects in bounds
    keep_in_bounds(player)
    keep_in_bounds(enemy)
    
    # Move enemy toward player slowly
    angle = angle_between(enemy['x'], enemy['y'], player['x'], player['y'])
    enemy['x'] += math.cos(angle) * 1
    enemy['y'] += math.sin(angle) * 1

def on_key_down(key):
    speed = 10
    if key == keys.LEFT:
        player['x'] -= speed
    elif key == keys.RIGHT:
        player['x'] += speed
    elif key == keys.UP:
        player['y'] -= speed
    elif key == keys.DOWN:
        player['y'] += speed
    elif key == keys.SPACE:
        # Create explosion at player position
        new_particles = create_explosion_particles(player['x'], player['y'])
        particles.extend(new_particles)
