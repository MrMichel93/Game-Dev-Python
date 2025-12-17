"""
Module 1 Example: Basic Game State with Variables
This demonstrates how variables represent and manage game state
"""

# Window dimensions
WIDTH = 800
HEIGHT = 600

# Player state variables
player_x = 400
player_y = 300
player_speed = 5

# Game state variables
score = 0
lives = 3
level = 1

def draw():
    """Draw the game state to the screen"""
    # Fill background
    screen.fill((0, 0, 0))  # Black background
    
    # Display game information
    screen.draw.text(f"Score: {score}", (10, 10), color="white", fontsize=30)
    screen.draw.text(f"Lives: {lives}", (10, 40), color="white", fontsize=30)
    screen.draw.text(f"Level: {level}", (10, 70), color="white", fontsize=30)
    
    # Draw player
    screen.draw.filled_circle((player_x, player_y), 20, "blue")

def update():
    """Update game state each frame"""
    global player_x
    
    # Move player right automatically
    player_x += player_speed
    
    # Wrap around screen when reaching edge
    if player_x > WIDTH:
        player_x = 0
