"""
Practice Problem 2: Fixed Score System
This is the corrected version with comments explaining the fixes
"""

# Fixed score system
WIDTH = 800
HEIGHT = 600

# Game variables
score = 0
bonus_points = 50
player_name = "Hero"  # Fixed Bug 1: Added quotes around string
high_score = 100

def draw():
    screen.fill((0, 0, 0))
    screen.draw.text(f"Player: {player_name}", (10, 10), color="white")
    screen.draw.text(f"Score: {score}", (10, 30), color="white")  # Fixed Bug 2: Changed Score to score (correct variable name)
    screen.draw.text(f"High Score: {high_score}", (10, 50), color="white")

def update():
    global score, high_score  # Fixed Bugs 3 & 4: Added global keyword for both variables
    
    # Add bonus points every frame
    score = score + bonus_points
    
    # Check if new high score
    if score > high_score:
        high_score = score
