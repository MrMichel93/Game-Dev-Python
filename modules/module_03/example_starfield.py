"""
Module 3 Example: Starfield Animation
Demonstrates loops for creating and animating multiple objects
"""
import random

WIDTH = 800
HEIGHT = 600

# Create list of stars using a loop
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
    
    # Instructions
    screen.draw.text("Scrolling starfield animation", 
                    (WIDTH/2 - 120, HEIGHT - 30), 
                    color="cyan", fontsize=20)

def update():
    # Update all stars using a loop
    for star in stars:
        # Move star down
        star['y'] += star['speed']
        
        # Reset star to top when it goes off bottom
        if star['y'] > HEIGHT:
            star['y'] = 0
            star['x'] = random.randint(0, WIDTH)
