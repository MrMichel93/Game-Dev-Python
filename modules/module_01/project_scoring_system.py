"""
Module 1 Project: Complete Scoring System
This is an example solution for the project task
"""

import random

WIDTH = 800
HEIGHT = 600

# Player variables
player_x = 400
player_y = 300
player_speed = 3
player_size = 25

# Game state variables
score = 0
high_score = 0
lives = 3
level = 1

# Collectible variables
collectible_x = random.randint(50, WIDTH - 50)
collectible_y = random.randint(50, HEIGHT - 50)
collectible_size = 15
collectible_points = 10

# Visual feedback
score_flash = 0  # Used to flash score when collecting

def draw():
    """Draw all game elements"""
    screen.fill((20, 20, 40))  # Dark blue background
    
    # Draw game state information
    screen.draw.text(f"Score: {score}", (10, 10), color="white", fontsize=30)
    screen.draw.text(f"High Score: {high_score}", (10, 45), color="yellow", fontsize=25)
    screen.draw.text(f"Lives: {lives}", (WIDTH - 120, 10), color="red", fontsize=30)
    screen.draw.text(f"Level: {level}", (WIDTH - 120, 45), color="cyan", fontsize=25)
    
    # Flash score when collecting (visual feedback)
    if score_flash > 0:
        screen.draw.text(f"+{collectible_points}!", 
                        (player_x, player_y - 40), 
                        color="green", 
                        fontsize=35)
    
    # Draw player
    screen.draw.filled_circle((player_x, player_y), player_size, "blue")
    screen.draw.circle((player_x, player_y), player_size, "white")
    
    # Draw collectible
    screen.draw.filled_circle((collectible_x, collectible_y), collectible_size, "gold")
    screen.draw.text(f"{collectible_points}", 
                    (collectible_x - 10, collectible_y - 5), 
                    color="black", 
                    fontsize=20)

def update():
    """Update game logic"""
    global player_x, player_y, score, high_score, collectible_x, collectible_y, score_flash
    
    # Auto-move player (in Module 7 we'll add keyboard control)
    player_x += player_speed
    
    # Wrap around screen
    if player_x > WIDTH + player_size:
        player_x = -player_size
    
    # Check collision with collectible
    distance = ((player_x - collectible_x) ** 2 + (player_y - collectible_y) ** 2) ** 0.5
    
    if distance < player_size + collectible_size:
        # Collect the item
        score += collectible_points
        score_flash = 30  # Flash for 30 frames
        
        # Update high score if needed
        if score > high_score:
            high_score = score
        
        # Respawn collectible at new location
        collectible_x = random.randint(50, WIDTH - 50)
        collectible_y = random.randint(50, HEIGHT - 50)
    
    # Decrease flash counter
    if score_flash > 0:
        score_flash -= 1
