"""
Practice Problem 3: Health System Starter Code
Students need to extend this code with armor and shield mechanics
"""

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
