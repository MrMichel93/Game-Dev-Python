"""
Practice Problem 2: Buggy Score System
Students need to find and fix the bugs in this code
"""

# Buggy score system
WIDTH = 800
HEIGHT = 600

# Game variables
score = 0
bonus_points = 50
player_name = Hero  # Bug 1: Missing quotes
high_score = 100

def draw():
    screen.fill((0, 0, 0))
    screen.draw.text(f"Player: {player_name}", (10, 10), color="white")
    screen.draw.text(f"Score: {Score}", (10, 30), color="white")  # Bug 2: Wrong variable name (capital S)
    screen.draw.text(f"High Score: {high_score}", (10, 50), color="white")

def update():
    # Add bonus points every frame
    score = score + bonus_points  # Bug 3: Missing global keyword
    
    # Check if new high score
    if score > high_score:
        high_score = score  # Bug 4: Missing global keyword
