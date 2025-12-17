"""
Practice Problem 2: Fixed Collision Detection
Corrected version with all bugs fixed
"""

# Fixed collision detection
WIDTH = 800
HEIGHT = 600

player_x = 100
player_y = 100
player_size = 30

enemy_x = 400
enemy_y = 300
enemy_size = 25

collision_detected = False

def draw():
    screen.fill((0, 0, 0))
    
    # Draw player
    screen.draw.filled_circle((player_x, player_y), player_size, "blue")
    
    # Draw enemy
    screen.draw.filled_circle((enemy_x, enemy_y), enemy_size, "red")
    
    # Fixed Bug 1: Removed redundant == True comparison
    if collision_detected:
        screen.draw.text("COLLISION!", (WIDTH/2 - 50, 50), color="yellow", fontsize=40)

def update():
    global player_x, collision_detected
    
    # Move player toward enemy
    player_x += 2
    
    # Fixed Bug 4: Added bounds checking to prevent going off screen
    if player_x > WIDTH + player_size:
        player_x = 0
    
    # Check collision
    distance = ((player_x - enemy_x) ** 2 + (player_y - enemy_y) ** 2) ** 0.5
    
    # Fixed Bugs 2 & 3: Changed > to < and swapped the logic
    if distance < player_size + enemy_size:
        collision_detected = True
    else:
        collision_detected = False
