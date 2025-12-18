"""
Module 3 Project: Weather Particle System (Rain/Snow)
Demonstrates comprehensive use of loops for particle effects
"""
import random

WIDTH = 800
HEIGHT = 600

# Weather modes
RAIN = "rain"
SNOW = "snow"

# Current settings
weather_mode = RAIN
wind = 0  # Horizontal wind force

# Create particles using a loop
particles = []
for i in range(150):
    particle = {
        'x': random.randint(0, WIDTH),
        'y': random.randint(-HEIGHT, HEIGHT),
        'speed': random.uniform(3, 8) if weather_mode == RAIN else random.uniform(1, 3),
        'size': random.randint(1, 3) if weather_mode == RAIN else random.randint(3, 6),
        'sway': random.uniform(-0.5, 0.5)  # Horizontal movement
    }
    particles.append(particle)

# Ground accumulation
ground_height = [0] * WIDTH

def draw():
    # Background color based on weather
    if weather_mode == RAIN:
        screen.fill((50, 50, 80))  # Dark blue
    else:
        screen.fill((200, 210, 220))  # Light gray
    
    # Draw accumulated ground
    for x in range(WIDTH):
        if ground_height[x] > 0:
            color = (150, 180, 200) if weather_mode == RAIN else (255, 255, 255)
            screen.draw.filled_rect(
                Rect(x, HEIGHT - ground_height[x], 1, ground_height[x]),
                color
            )
    
    # Draw all particles using a loop
    for particle in particles:
        if weather_mode == RAIN:
            # Draw rain as lines
            screen.draw.line(
                (particle['x'], particle['y']),
                (particle['x'] - particle['speed']/2, particle['y'] + particle['speed']*2),
                (100, 150, 255)
            )
        else:
            # Draw snow as circles
            screen.draw.filled_circle(
                (int(particle['x']), int(particle['y'])),
                particle['size'],
                "white"
            )
    
    # Display info
    screen.draw.text(f"Weather: {weather_mode.upper()}", 
                    (10, 10), color="white", fontsize=30)
    screen.draw.text(f"Particles: {len(particles)}", 
                    (10, 45), color="white", fontsize=25)
    screen.draw.text(f"Wind: {wind:.1f}", 
                    (10, 75), color="white", fontsize=25)
    screen.draw.text("Press R for Rain, S for Snow", 
                    (10, HEIGHT - 60), color="white", fontsize=20)
    screen.draw.text("Arrow keys control wind", 
                    (10, HEIGHT - 30), color="white", fontsize=20)

def update():
    global wind
    
    # Apply wind decay
    wind *= 0.95
    
    # Update all particles using a loop
    for particle in particles:
        # Move particle down
        particle['y'] += particle['speed']
        
        # Apply wind and sway
        particle['x'] += wind + particle['sway']
        
        # Wrap horizontally
        if particle['x'] < 0:
            particle['x'] = WIDTH
        elif particle['x'] > WIDTH:
            particle['x'] = 0
        
        # Check if particle reaches ground
        if particle['y'] >= HEIGHT - 5:
            # Add to ground accumulation
            x_pos = int(particle['x'])
            if 0 <= x_pos < WIDTH and ground_height[x_pos] < 50:
                if weather_mode == SNOW:
                    ground_height[x_pos] += 1
                
                # Create splash effect for rain
                if weather_mode == RAIN:
                    create_splash(particle['x'], HEIGHT)
            
            # Reset particle to top
            particle['y'] = random.randint(-50, -10)
            particle['x'] = random.randint(0, WIDTH)

def create_splash(x, y):
    """Create small splash particles (simplified)"""
    pass  # Could add splash particles here

def on_key_down(key):
    global weather_mode, wind, particles
    
    # Change weather mode
    if key == keys.R:
        weather_mode = RAIN
        # Update particle properties for rain
        for particle in particles:
            particle['speed'] = random.uniform(3, 8)
            particle['size'] = random.randint(1, 3)
    elif key == keys.S:
        weather_mode = SNOW
        # Update particle properties for snow
        for particle in particles:
            particle['speed'] = random.uniform(1, 3)
            particle['size'] = random.randint(3, 6)
    
    # Control wind
    elif key == keys.LEFT:
        wind -= 2
    elif key == keys.RIGHT:
        wind += 2
    
    # Reset ground
    elif key == keys.C:
        for i in range(WIDTH):
            ground_height[i] = 0
